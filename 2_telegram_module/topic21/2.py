import os
import time

import telebot
from telebot import types
from telebot import util
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_command_handler(message):

    markup = types.InlineKeyboardMarkup()

    item1 = types.InlineKeyboardButton("Алматы", callback_data="almaty")
    item2 = types.InlineKeyboardButton("Астана", callback_data="astana")

    markup.add(item1, item2)

    bot.send_message(
        chat_id=message.chat.id,
        text="Начинаем!\nНажмите кнопку!",
        reply_markup=markup
    )


@bot.message_handler(commands=['start_test'])
def start_command_handler(message):

    markup = util.quick_markup(
        {
            'Алматы': {'callback_data': 'almaty'},
            'Астана': {'callback_data': 'astana'}
        }
    )

    bot.send_message(
        chat_id=message.chat.id,
        text="Начинаем!\nНажмите кнопку!",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    print(f"type of call: {type(call)}")
    print(f"{call.data=}")

    bot.answer_callback_query(
        callback_query_id=call.id,
        text="Отлично, спасибо за ответ!",
        show_alert=False
    )

    if call.data == 'astana':
        reply_text = 'Холодно же!'
    elif call.data == 'almaty':
        reply_text = 'Декабрь, а снега нет('

    bot.send_message(
        chat_id=call.message.chat.id,
        text=reply_text
    )

    bot.send_message(
        chat_id=call.message.chat.id,
        text=call.message.text
    )

@bot.message_handler(content_types=["text"])
def text_message_handler(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Принял текст!"
    )


bot.polling()
