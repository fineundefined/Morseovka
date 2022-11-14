import os
from Morse import *
from GetFile import *
from TeamName import *
import telebot

bot = telebot.TeleBot('5614828416:AAF4WNZqZf1_BRqmDPFQIwye5CEft5a0MPY')

if __name__ == "__main__":
    os.system("title Morseovka")
    os.system("mode con cols=101 lines=30")

bot.set_my_commands([
    telebot.types.BotCommand("/encode", "'/encode + text'"),
    telebot.types.BotCommand("/decode", "/decode + morse code")
])


@bot.message_handler(commands=['/encode', '/decode'])
def send_info_message(message):
    if message.text == "/encode":
        bot.send_message(message, "write some text to encode")
    elif message.text == "/decode":
        bot.send_message(message, "write morse code to decode")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user_Input = message.text
    user_Input = user_Input.split(" ", 1)
    fisrt_command = user_Input[0]
    del user_Input[0]

    user_Input = ''.join(user_Input)
    dot = '.'
    dash = '-'
    try:
        user_Input = user_Input.split(' /', 2)
        dot = user_Input[1]
        dash = user_Input[2]
        del user_Input[1:3]
    except:
        pass

    print(message.from_user.first_name, "[", message.from_user.id, "]:", message.text)

    if user_Input[0] != "":

        match fisrt_command:
            case "/decode":
                user_Input = ' '.join(user_Input)

                print("decoding from morse code\n")
                bot.send_message(message.from_user.id, Morse.decodeMorse(user_Input, dot, dash))
            case "/encode":
                user_Input = ' '.join(user_Input)

                print("encoding from morse code\n")
                bot.send_message(message.from_user.id, Morse.encodeMorse(user_Input, dot, dash))

            case _:
                bot.send_message(message.from_user.id, "Command is incorrect")
    else:
        bot.send_message(message.from_user.id, "You cannot encode or decode nothing")


bot.polling(none_stop=True, interval=0)
