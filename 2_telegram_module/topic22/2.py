import os
import time

import telebot
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["kick"])
def command_handler(message):

    try:
        admins_of_chat = bot.get_chat_administrators(message.chat.id)
        if message.from_user.id not in [admin.user.id for admin in admins_of_chat]:
            raise Exception('Ты не админ!')

        for admin in admins_of_chat:
            print(admin.user.username)

        user_to_kick = message.reply_to_message.from_user

        bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_kick.id
        )

        bot.send_message(
            chat_id=message.chat.id,
            text=f"Команду принял, Из группы удалил @{user_to_kick.username}!"
        )
    except Exception as e:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Error: {e}"
        )


bot.polling()

