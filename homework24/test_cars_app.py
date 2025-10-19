import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

# === Налаштування логування ===
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# лог у консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# лог у файл
file_handler = logging.FileHandler("test_search.log", mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@pytest.fixture(scope="class")
def auth_session():
    """Фікстура створює сесію, проходить логін і додає токен у заголовки."""
    session = requests.Session()
    auth_url = "http://127.0.0.1:8080/auth"

    response = session.post(auth_url, auth=HTTPBasicAuth("test_user", "test_pass"))
    assert response.status_code == 200, "Помилка аутентифікації"

    token = response.json().get("access_token")
    assert token, "Токен не отримано!"

    session.headers.update({"Authorization": f"Bearer {token}"})
    logger.info("Отримано токен доступу.")
    return session


@pytest.mark.parametrize("sort_by,limit", [
    ("price", 3),
    ("year", 5),
    ("engine_volume", 4),
    ("brand", 10),
    ("price", 1),
    ("year", 7),
    ("engine_volume", 2),
])
def test_get_cars(auth_session, sort_by, limit):
    """Тестує отримання списку автомобілів з різними параметрами."""
    url = f"http://127.0.0.1:8080/cars?sort_by={sort_by}&limit={limit}"
    logger.info(f"Виконуємо запит: {url}")

    response = auth_session.get(url)
    logger.info(f"Отримано статус-код: {response.status_code}")

    assert response.status_code == 200, f"Невірний код відповіді для sort_by={sort_by}, limit={limit}"

    data = response.json()
    assert isinstance(data, list), "Очікується список результатів"
    assert len(data) <= int(limit), f"Повернуто забагато записів ({len(data)} замість {limit})"

    logger.info(f"✓ Перевірено sort_by={sort_by}, limit={limit}, отримано {len(data)} записів.\n")
