import telebot
bot = telebot.TeleBot('2055137279:AAHhTlFtXG8-fEDnumakM61XPKPrkDRZNEU')

@bot.message_handler(content_types=['text','photo'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_photo(message.from_user.id,"https://sun9-39.userapi.com/impg/2Tg4WIvnOrmYsIZIHfamTuxqY1Z_cYBwYOyOJA/xDh-Uwd7ZTk.jpg?size=814x841&quality=96&sign=92b60b81ce81d3a49cefd7f904599db6&type=album")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.infinity_polling()