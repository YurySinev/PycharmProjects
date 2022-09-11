import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


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
