import imp
import telebot
import requests
import json

TOKEN = '5386412319:AAGoNUgj71uclssOgkm6dsBF3BSOlTJsus8'

bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'солана': 'SOL',
    'доллар': 'USDT',
    'рубль': 'RUR'
}


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


# @bot.message_handler()
# def echo_test(message: telebot.types.Message):
#    bot.send_message(message.chat.id, 'Привет!')

# обработка команд start и help:


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n \
<имя валюты>  <в какую валюту перевести>  <количество переводимой валюты>\n\
Список доступных валют: /values'
    bot.reply_to(message, text)


# выведение списка доступных валют:


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


# инфо о курсе валютной пары:


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    # поместили текст входящего сообщения в отдельную переменную
    values = message.text.split(' ')

    if len(values) != 3:  # если пользователь ввел более трех параметров
        raise ConvertionException("Слишком много параметров")

    quote, base, amount = values
    total_base = CryptoConverter.convert(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()
