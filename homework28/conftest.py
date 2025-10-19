# conftest.py — полный рабочий вариант

import os, sys, time, uuid, logging, pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === подключаем PageObject-локаторы из ./pages ===
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from pages.main_page import MainPageLocators
from pages.register_page import RegisterPageLocators


# ---------------- ЛОГИ ----------------
@pytest.fixture(scope="session", autouse=True)
def _logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("logs/test_registration.log", encoding="utf-8", mode="a"),
        ],
    )
    logging.info("=== START SESSION ===")
    yield
    logging.info("=== END SESSION ===")


# ---------------- ДРАЙВЕР ----------------
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Если окно мешает — раскомментируй headless:
    # options.add_argument("--headless=new")
    # Ускорители/стабильность:
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


# ---------------- БАЗА ----------------
@pytest.fixture(scope="session")
def base_url():
    # Доступ с basic-auth согласно заданию
    return "https://guest:welcome2qauto@qauto2.forstudy.space/"

@pytest.fixture(scope="session")
def main_locators():
    return MainPageLocators

@pytest.fixture(scope="session")
def register_locators():
    return RegisterPageLocators

@pytest.fixture()
def wait(driver):
    return WebDriverWait(driver, 20)


# ---------------- ВСПОМОГАТЕЛЬНЫЕ ШАГИ ----------------
@pytest.fixture()
def open_site(driver, base_url):
    driver.get(base_url)
    # мелкая пауза на первичную анимацию
    time.sleep(1)
    yield

@pytest.fixture()
def accept_cookies(driver, wait):
    # Закрыть возможные куки-баннеры (несколько типичных вариантов)
    candidates = [
        (By.CSS_SELECTOR, "button#rcc-confirm-button"),
        (By.CSS_SELECTOR, "[data-testid='accept-privacy'], [data-testid='cookie-accept']"),
        (By.XPATH, "//button[contains(.,'Accept') or contains(.,'Принять') or contains(.,'Погоджуюсь')]"),
    ]
    for loc in candidates:
        try:
            btn = wait.until(EC.element_to_be_clickable(loc))
            btn.click()
            logging.info("Cookie banner accepted")
            break
        except Exception:
            pass
    yield

@pytest.fixture()
def go_to_signup(driver, wait, base_url, main_locators, register_locators, accept_cookies):
    """
    Сначала пытаемся открыть форму регистрации напрямую по URL.
    Если не вышло — пробуем кликать по кнопкам/ссылкам Sign up.
    """
    def page_has_form():
        try:
            wait.until(EC.visibility_of_element_located(register_locators.FIRSTNAME))
            return True
        except Exception:
            return False

    # 1) Прямые URL, самые частые варианты SPA/маршрутов
    direct_urls = [
        base_url + "#/signup",
        base_url + "signup",
        base_url + "auth/signup",
        base_url + "#/registration",
        base_url + "panel/register",
    ]
    for url in direct_urls:
        try:
            driver.get(url)
            if page_has_form():
                logging.info(f"Signup form opened directly: {url}")
                yield
                return
        except Exception:
            continue

    # 2) Fallback: с главной страницы пробуем клики по «Sign up»
    driver.get(base_url)
    time.sleep(1)
    actions = ActionChains(driver)

    def safe_click(locator):
        el = wait.until(EC.element_to_be_clickable(locator))
        actions.move_to_element(el).pause(0.2).click().perform()

    tried = []
    try:
        safe_click(main_locators.SIGNUP_BTN); tried.append("SIGNUP main")
        if page_has_form():
            logging.info("Signup form opened via SIGNUP main")
            yield
            return
    except Exception:
        pass

    # запасные клики по текстам/селектору
    fallbacks = [
        (By.CSS_SELECTOR, "a[href*='signup'], button[data-testid='signup']"),
        (By.XPATH, "//a[contains(.,'Sign up') or contains(.,'Зареєструватись') or contains(.,'Реєстрація')]"),
        (By.XPATH, "//button[contains(.,'Sign up') or contains(.,'Зареєструватись') or contains(.,'Реєстрація')]"),
    ]
    for loc in fallbacks:
        try:
            safe_click(loc); tried.append("fallback")
            if page_has_form():
                logging.info("Signup form opened via fallback")
                yield
                return
        except Exception:
            continue

    # 3) Через Login-модалку (часто внутри есть ссылка на регистрацию)
    try:
        safe_click(main_locators.LOGIN_BTN); tried.append("login open")
        inner = (By.XPATH, "//a[contains(.,'Sign up') or contains(.,'Зареєструватись') or contains(.,'Реєстрація')]")
        safe_click(inner); tried.append("login->signup")
        if page_has_form():
            logging.info("Signup form opened via login modal")
            yield
            return
    except Exception as e:
        pass

    # Если ничего не помогло — сохраняем артефакты и падаем
    driver.save_screenshot("debug_signup.png")
    with open("debug_signup.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    raise TimeoutError(f"Не удалось открыть форму регистрации. Пробовали: {tried}")


@pytest.fixture()
def new_user():
    uid = uuid.uuid4().hex[:8]
    return {
        "first": "Test",
        "last": "User",
        "email": f"test_{uid}@example.com",
        "password": "QAuto_12345",
    }

@pytest.fixture()
def fill_registration_form(driver, register_locators, wait, new_user):
    wait.until(EC.visibility_of_element_located(register_locators.FIRSTNAME)).send_keys(new_user["first"])
    wait.until(EC.visibility_of_element_located(register_locators.LASTNAME)).send_keys(new_user["last"])
    wait.until(EC.visibility_of_element_located(register_locators.EMAIL)).send_keys(new_user["email"])
    wait.until(EC.visibility_of_element_located(register_locators.PASSWORD)).send_keys(new_user["password"])
    wait.until(EC.visibility_of_element_located(register_locators.REPASSWORD)).send_keys(new_user["password"])
    # чекбокс политики — если есть
    try:
        cb = wait.until(EC.element_to_be_clickable(register_locators.POLICY_CHECK))
        if not cb.is_selected():
            cb.click()
    except Exception:
        pass
    logging.info(f"Form filled for email: {new_user['email']}")
    yield new_user

@pytest.fixture()
def submit_registration(driver, register_locators, wait):
    wait.until(EC.element_to_be_clickable(register_locators.REGISTER_BTN)).click()
    logging.info("Register button clicked")
    time.sleep(1)
    yield

@pytest.fixture()
def check_success(driver, register_locators, wait):
    ok = False
    # 1) тост/алерт об успехе
    try:
        wait.until(EC.presence_of_element_located(register_locators.SUCCESS_TOAST))
        ok = True
        logging.info("SUCCESS toast detected")
    except Exception:
        # 2) редирект в личный кабинет (по URL)
        if any(x in driver.current_url for x in ["garage", "panel", "app"]):
            ok = True
            logging.info("URL indicates successful registration")
        else:
            logging.warning("No explicit success indicator found")
    yield ok


# ---------------- Композитная фикстура для теста ----------------
@pytest.fixture()
def registration_result(open_site, accept_cookies, go_to_signup,
                        fill_registration_form, submit_registration, check_success):
    return check_success  # True/False
