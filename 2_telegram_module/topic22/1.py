import os
import time

import telebot
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["hello"])
def command_handler(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Команду принял!"
    )


@bot.message_handler(func=lambda message: message.reply_to_message is not None
                                          and 'спасибо' in message.text
                                          and message.reply_to_message.from_user.is_bot is True)
def replied_message_handler(message):
    bot.reply_to(
        message=message,
        text='Не за что!'
    )


# @bot.message_handler(func=lambda message: message.text)
# def replied_message_handler(message):
#     bot.reply_to(
#         message=message,
#         text=f'test @{message.from_user.username}!'
#     )


@bot.message_handler(func=lambda message: message.new_chat_members is not None or message.left_chat_member is not None)
def echo_handler(message):
    new_members = message.new_chat_members
    new_members.extend(message.left_chat_member)
    print(new_members)
    print(f"type of new_members: {type(new_members)}")
    for member in new_members:
        print(f"type of member: {type(member)}")

        bot.send_message(
            chat_id=message.chat.id,
            text=f"Привет или Пока, @{member.username}!"
        )


@bot.message_handler(func=lambda message: 'привет' in message.text and 'бот' in message.text)
def echo_handler(message):
    print(message.new_chat_members)

    bot.reply_to(
        message=message,
        text=f"Привет, {message.from_user.first_name}!"
    )



bot.polling()
