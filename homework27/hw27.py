from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NovaPoshtaTracker:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open_page(self):
        self.driver.get(self.url)
        time.sleep(2)  # ждём прогрузки JS

    def track_parcel(self, tracking_number: str) -> str:
        # Ждём появления поля ввода
        input_field = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder*='накладної']"))
        )
        input_field.clear()
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.ENTER)

        # Ждём появления любого блока с результатом (или ошибки)
        time.sleep(2)  # небольшой таймаут для обновления страницы
        try:
            status_block = self.driver.find_element(
                By.CSS_SELECTOR, "div.header__parcel-dynamic-status div.header__status-text"
            )
            return status_block.text
        except:
            # Если блок со статусом не найден — возвращаем сообщение о неверной накладной
            return "Посилка не знайдена"


# --- Пример использования ---
if __name__ == "__main__":
    driver = webdriver.Chrome()
    tracker = NovaPoshtaTracker(driver)
    tracker.open_page()

    test_number = "0000000000"  # рандомный номер
    actual_status = tracker.track_parcel(test_number)
    print("Статус:", actual_status)

    driver.quit()
