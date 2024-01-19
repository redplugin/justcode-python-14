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

    markup = types.InlineKeyboardMarkup(row_width=3)

    item1 = types.InlineKeyboardButton("Алматы", callback_data="almaty")
    item2 = types.InlineKeyboardButton("Астана", callback_data="astana")
    item3 = types.InlineKeyboardButton("Посмотреть кино", url="https://google.com/")
    item4 = types.InlineKeyboardButton("Тараз", callback_data="taraz")

    markup.add(item1, item2, item3, item4)

    bot.send_message(
        chat_id=message.chat.id,
        text="Начинаем!\nНажмите кнопку!",
        reply_markup=markup
    )

# @bot.message_handler(commands=['start'])
# def start_command_handler(message):
#
#     markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
#     # markup = types.ReplyKeyboardMarkup(row_width=3)
#
#     item1 = types.KeyboardButton("Алматы")  # CTRL + d
#     item2 = types.KeyboardButton("Астана")
#     item3 = types.KeyboardButton("Караганды")
#     item4 = types.KeyboardButton("Тараз")
#
#     markup.add(item1, item2, item3, item4)
#
#     bot.send_message(
#         chat_id=message.chat.id,
#         text="Начинаем!\nНажмите кнопку!",
#         reply_markup=markup
#     )
#


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    print(f"type of call: {type(call)}")
    print(f"{call.data=}")

    bot.answer_callback_query(
        callback_query_id=call.id,
        text="Отлично, спасибо за ответ!",
        show_alert=False
    )


filenames = {
    "f": "file_name",
    "c": "file_name2"
}

@bot.message_handler(content_types=["text"])
def text_message_handler(message):

    bot.send_message(
        chat_id=message.chat.id,
        text="Принял текст!"
    )




bot.polling()
