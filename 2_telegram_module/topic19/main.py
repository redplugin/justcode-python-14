import time

import telebot

API_TOKEN = "6647028355:AAH-mEdNesie3Lj1eMQ_wyr0L0u8o7juhL4"

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'justcode'])
def commands_message(message):
    print("тип полученного сообщение:", message.content_type)

    # bot.send_message(chat_id=message.chat.id, text="Понял команду!")
    bot.reply_to(message, text="Понял команду!")


@bot.message_handler(func=lambda msg: True)
# @bot.message_handler(func=lambda msg: "test" in msg.text)
def repeat_all_messages(message):
    print("тип полученного сообщение:", message.content_type)

    if message.text == "Привет":
        otvet = "Привет:)"
    elif message.text == "Пока!":
        otvet = "Пока, рад был познакомиться"
    else:
        otvet = "Я тебя не понимаю!"

    msg = bot.send_message(chat_id=message.chat.id, text=otvet)
    time.sleep(4)
    bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
    bot.send_message(chat_id=message.chat.id, text="Ha-Ha-Ha-Ha-Ha-Ha-Ha-Ha-Ha")



@bot.message_handler(func=lambda msg: "photo" in msg.text)
def sending_photo(message):
    print("тип полученного сообщение:", message.content_type)

    # bot.send_message(chat_id=message.chat.id, text=otvet)
    # bot.send_photo(chat_id=message.chat.id, photo=open("data/img1.jpg", 'rb'))
    bot.send_document(chat_id=message.chat.id, document=open("data/img1.jpg", 'rb'))


@bot.message_handler(content_types=["photo", "document"])
def sending_photo(message):
    print("тип полученного сообщение:", message.content_type)


    # bot.send_message(chat_id=message.chat.id, text=otvet)
    # bot.send_photo(chat_id=message.chat.id, photo=open("data/img1.jpg", 'rb'))
    # bot.send_document(chat_id=message.chat.id, document=open("data/img1.jpg", 'rb'))

    photo = message.photo[-1]  # Get the last photo in the list
    file_id = photo.file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path

    # Save the photo locally
    downloaded_file = bot.download_file(file_path)
    with open(f"data/img3.txt", 'wb') as new_file:
        new_file.write(downloaded_file)
    #
    # bot.send_photo(chat_id=message.chat.id, photo=open(f"data/img3.txt", 'rb'))
    bot.send_photo(chat_id=message.chat.id, photo=file_id)
    # bot.send_photo(chat_id=message.chat.id, photo=downloaded_file)


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    # Extract sticker details
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji

    # Reply with a message indicating that a sticker has been received
    reply_text = f"Received a sticker! Sticker ID: {sticker_id}\nEmoji: {emoji}"
    bot.reply_to(message, reply_text)

    # sticker_file_id = "YOUR_STICKER_FILE_ID"

    # Send the sticker
    bot.send_sticker(message.chat.id, sticker_id)



bot.polling()
# bot.infinity_polling()
