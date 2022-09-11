import requests
import json
from config import keys

class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:  # если пользователь ввел одну и ту же валюту
            raise ConvertionException(
                f"Невозможно перевести одинаковые валюты {base}")

        try:  # заведем тикеры для обозначения валют и проверим правильность ввода
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

        try:  # то же самое для второй валюты
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:  # обработка неверного количества
            amount = float(amount)
        except ValueError:
            raise ConvertionException(
                f"Не удалось обработать количество {amount}")

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
