import telebot

TOKEN = "1680972792:AAEaZO68WjS0ZRqKXojW6Zv0j2ptxfeV_F0"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f"Приветствую тебя, о <b>{message.chat.first_name} {message.chat.last_name}</b>!", parse_mode='html')


# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     bot.send_message(message, "Приветствую тебя,")

@bot.message_handler(content_types=['voice'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "У тебя красивый голос")


@bot.message_handler(content_types=['photo'])
def get_user_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Ух ты! Крутое фото!')


# @bot.message_handler(content_types=['text'])
# def say_hello(message: telebot.types.Message):
#     bot.reply_to(message, f"Я тоже рад поговорить с тобой, {message.chat.username}")


@bot.message_handler()
def message_info(message):
    bot.send_message(message.chat.id, message, parse_mode='html')


bot.infinity_polling()

