import json

import requests

from config import API_KEY


def get_currency_rate(from_: str, to: str) -> float | None:
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={from_}"
    response = requests.get(url, headers={'apikey': API_KEY})
    response_data = json.loads(response.text)
    rate = response_data['rates'][to]
    return rate

def currency_converter(rate, value):
    return rate * value