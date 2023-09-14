from fastapi import FastAPI

from utils import get_currency_rate, currency_converter

app = FastAPI(
    title='Тестовое задание "Конвертер валют"',
    description='Тестовое задание "Конвертер валют"',
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/rates")
def get_rates(from_: str, to: str, value: int):
    rate = get_currency_rate(from_, to)
    result = currency_converter(rate, value)
    return {"result": result}
