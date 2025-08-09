import json
import logging

logging.basicConfig(level=logging.ERROR)
try:
    with open("localizations_en.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    logging.error('Невалідний файл 1')
try:
    with open("localizations_ru.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    logging.error('Невалідний файл 2')
try:
    with open("login.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    logging.error('Невалідний файл 3')
try:
    with open("swagger.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    logging.error('Невалідний файл 4')

