import os
import time

import telebot
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["test_command"])
def command_handler(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Команду принял!"
    )


@bot.message_handler(content_types=["text"])
def text_message_handler(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=message.text
    )


@bot.message_handler(content_types=["document"])
def document_message_handler(message):
    msg = bot.send_message(
        chat_id=message.chat.id,
        text="Ожидайте..."
    )

    document = message.document

    file_id = document.file_id
    file_info = bot.get_file(file_id)
    downloaded_file_binary = bot.download_file(file_info.file_path)

    with open(f"downloads/{document.file_name}", 'wb') as file:
        file.write(downloaded_file_binary)

    bot.send_document(
        chat_id=message.chat.id,
        document=open(f"downloads/{document.file_name}", 'rb')
    )
    bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)


@bot.message_handler(content_types=["photo"])
def document_message_handler(message):

    document = message.photo[-1]
    file_id = document.file_id

    bot.send_photo(
        chat_id=message.chat.id,
        photo=file_id
    )



# @bot.message_handler(content_types=["photo"])
# def document_message_handler(message):
#     msg = bot.send_message(
#         chat_id=message.chat.id,
#         text="Ожидайте..."
#     )
#
#     document = message.photo[-1]
#     file_id = document.file_id
#     file_info = bot.get_file(file_id)
#     downloaded_file_binary = bot.download_file(file_info.file_path)
#
#     file_name = f"test_photo_{time.time()}.jpg"
#
#     with open(f"downloads/{file_name}", 'wb') as file:
#         file.write(downloaded_file_binary)
#
#     bot.send_photo(
#         chat_id=message.chat.id,
#         photo=open(f"downloads/{file_name}", 'rb'),
#         caption="test caption 1"
#     )
#     bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)


# @bot.message_handler(content_types=["document", "photo"])
# def document_message_handler(message):
#
#     if message.document is not None:
#         document = message.document
#         file_name = document.file_name
#     elif message.photo is not None:
#         document = message.photo[-1]
#         file_name = f"test_photo_{time.time()}.jpg"
#
#     file_id = document.file_id
#     file_info = bot.get_file(file_id)
#     downloaded_file_binary = bot.download_file(file_info.file_path)
#
#     with open(f"downloads/{file_name}", 'wb') as file:
#         file.write(downloaded_file_binary)
#
#     bot.send_message(
#         chat_id=message.chat.id,
#         text="Принял документ и сохранил у себя!"
#     )


bot.polling()





