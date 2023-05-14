import telebot
from telebot import types
import config
import requests
import json

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.kstu.ru/"))
    bot.send_message(message.chat.id, "Перейдите на сайт", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(message.chat.id, "Выбирите действие", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    city = message.text.strip().lower()
    res = requests.get(f'наш юрл')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message,f'Данный запрос выполнен: {temp}')
    else:
        bot.reply_to(message, f'Такой комманды нету')
#RUN
bot.polling(none_stop=True)