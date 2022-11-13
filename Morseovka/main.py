import os
from Morse import *
from GetFile import *
from TeamName import *
import telebot

bot = telebot.TeleBot('TOKEN')

if __name__ == "__main__":
    os.system("title Morseovka")
    os.system("mode con cols=101 lines=30")

bot.set_my_commands([
    telebot.types.BotCommand("/decode", "'/decode + text'"),
    telebot.types.BotCommand("/encode", "'/encode + text'")
])

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    userInput = message.text
    write_message_fun(userInput,message)


def write_message_fun(userInput,message):
    splitted_user_input = userInput.split(" ", 1)
    print(message.from_user.first_name, message.text)

    if splitted_user_input[0] == '/decode':
        del splitted_user_input[0]
        splitted_user_input = ' '.join(splitted_user_input)

        print("decoding from morse code\n")
        bot.send_message(message.from_user.id, Morse.decodeMorse(splitted_user_input))

    elif splitted_user_input[0] == "/encode":

        del splitted_user_input[0]
        splitted_user_input = ' '.join(splitted_user_input)

        print("encoding from morse code\n")
        bot.send_message(message.from_user.id, Morse.encodeMorse(splitted_user_input))

    elif splitted_user_input[0] == "/file":
        del splitted_user_input[0]
        splitted_user_input = ' '.join(splitted_user_input)
        fileTEXT = GetFile.GetTextFromTXT(splitted_user_input)

        if fileTEXT != FileNotFoundError:
            inputChoose = (input("Decode text in file or encode [d/e]"))

            if inputChoose == "d":

                print("decoding from morse code\n")
                print(Morse.decodeMorse(fileTEXT), "\n")

            elif inputChoose == "e":

                print("encoding to morse code\n")

                print(Morse.encodeMorse(fileTEXT), "\n")

            else:
                print("!" * 99)
                print(
                    "File adress is incorrect!\nTry other forms of address(C:\\\..\\\..\\\ | C:\..\..\ | C:/../../) or check if the address is correct"
                )
                print("!" * 99, "\n")


bot.polling(none_stop=True, interval=0)
