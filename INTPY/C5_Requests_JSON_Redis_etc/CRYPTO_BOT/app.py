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
    try:
        values = message.text.split(' ')  # входящее сообщение - в отдельную переменную

        if len(values) != 3:  # если пользователь ввел более трех параметров
            raise ConvertionException("Число параметров должно быть 3:\nвалюта валюта сумма")

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка:\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
