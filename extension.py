import json

import requests

from config import currency


class ConversionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(values):
        base, quote, amount = values  # [0], values[1], values[2]
        if base == quote:
            raise ConversionException('Введены одинаковые валюты')
        try:
            base_ticker = currency[base]
        except KeyError:
            raise ConversionException(f'Невозможно обработать валюту{base}')
        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise ConversionException(f'Невозможно обработать валюту{quote}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException('Для обмена надо ввести число. Это не число.')
        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')  # ,EUR')
        # text=r.content
        rate = json.loads(r.content)[currency[quote]]

        return rate
    @staticmethod
    def get_rate(values):
        base, quote, amount = values
        rate = CryptoConverter.convert(values)
        text = f' Курс {base} к {quote} = {rate}\n'
        return text
