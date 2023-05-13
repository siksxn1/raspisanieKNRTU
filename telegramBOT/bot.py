import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['start'])
def welcome(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['text'])
def hello(message):
    bot.send_message(message.chat.id, message.text)

#RUN
bot.polling(none_stop=True)