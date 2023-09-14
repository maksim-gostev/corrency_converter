# Сервис "Конвертер валют"

## Используемые технологии

- [FastAPI](https://fastapi.tiangolo.com/)
- [Requests](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Json](https://docs.python.org/3/library/json.html)

### Функционал
- `GET /api/rates?from_=USD&to=RUB&value=1` 
- `from_ - из какой валюты`
- `to - в какую валюту`
- `value - количество валюты`

## Запуск
1. Создайте файл `.env`: скопируйте содержимое `.env_example` в новый файл `.env` в корневом каталоге проекта.
2.  Запустите приложение FastAPI:
   ```bash
   uvicorn main:app --reload
   ```