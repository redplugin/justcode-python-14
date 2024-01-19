import os
import time

import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_command_handler(message):

    markup = types.ReplyKeyboardMarkup()

    item1 = types.KeyboardButton("Алматы")  # CTRL + d
    item2 = types.KeyboardButton("Астана")

    markup.add(item1, item2)

    bot.send_message(
        chat_id=message.chat.id,
        text="Начинаем!\nНажмите кнопку!",
        reply_markup=markup
    )

#
# @bot.message_handler(commands=['astana'])
# def astana_command_handler(message):
#
#     bot.send_message(
#         chat_id=message.chat.id,
#         text="astana as command"
#     )


@bot.message_handler(func=lambda msg: msg.text in ['Алматы', 'Астана'])
def text_message_handler(message):
    if message.text == 'Астана':
        reply_text = 'Холодно же!'
    elif message.text == 'Алматы':
        reply_text = 'Декабрь, а снега нет('

    markup = types.ReplyKeyboardRemove()

    # markup = types.ReplyKeyboardMarkup()

    # item1 = types.KeyboardButton("Караганды")  # CTRL + d
    # item2 = types.KeyboardButton("Тараз")

    # markup.add(item1, item2)

    bot.send_message(
        chat_id=message.chat.id,
        text=reply_text,
        reply_markup=markup
    )


@bot.message_handler(content_types=["text"])
def text_message_handler(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Нужно нажать кнопку!"
    )


bot.polling()
