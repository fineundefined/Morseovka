import os
from Morse import Morse
import telebot


"""set bot token"""
bot = telebot.TeleBot('5696255478:AAEAwdmjdxRk1vpslUZmEp2I3QhcRRlOK50')

"""main function start"""
if __name__ == "__main__":
    """set console name"""
    os.system("title Morseovka")
    """set console size"""
    os.system("mode con cols=101 lines=30")
"""set the list of bot commands"""
bot.set_my_commands([
    telebot.types.BotCommand("/encode", "'/encode + text'"),
    telebot.types.BotCommand("/decode", "/decode + morse code")
])


"""new user message processing function"""


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Add message text to variable."""
    user_Input = message.text

    """create a list from the text of the
    message with the separator " " with maximum separation 1"""
    user_Input = user_Input.split(" ", 1)

    """add the first command to the variable"""
    fisrt_command = user_Input[0]

    """remove the first command from the list"""
    del user_Input[0]

    """create a string from a list"""
    user_Input = ''.join(user_Input)

    """set the default dot value(then I'll change it)"""
    dot = '.'

    """set the default dash value"""
    dash = '-'

    """we are trying to split the string again
    and set the values of the dot and dash
    to those that the user sent in the message"""
    try:
        user_Input = user_Input.split(' /', 2)
        dot = user_Input[1]
        dash = user_Input[2]
        del user_Input[1:3]

        """if there were no values in the message,
        then skip this step"""
    except IndexError:
        pass

    """Morse code list"""
    morse_code = {dot + dash + dot * 3: "&",
                  dash * 2 + dot * 2 + dash * 2: ",",
                  dot * 4 + dash: "4", dot * 5: "5",
                  dot * 5: "5",
                  dot * 3 + dash * 3 + dot * 3: "SOS",
                  dash + dot * 3: "B",
                  dash + dot * 2 + dash: "X",
                  dot + dash + dot: "R",
                  dot + dash * 2: "W",
                  dot * 2 + dash * 3: "2",
                  dot + dash: "A",
                  dot * 2: "I",
                  dot * 2 + dash + dot: "F",
                  dot: "E", dot + dash + dot * 2: "L",
                  dot * 3: "S", dot * 2 + dash: "U",
                  dot * 2 + dash * 2 + dot * 2: "?",
                  dot + dash * 4: "1", dash + dot + dash: "K",
                  dash + dot + dot: "D",
                  dash + dot * 4: "6", dash + dot * 3 + dash: "=",
                  dash * 3: "O", dot + dash * 2 + dot: "P",
                  dot + dash + dot + dash + dot + dash: ".",
                  dash * 2: "M", dash + dot: "N", dot * 4: "H",
                  dot + dash * 4 + dot: "'", dot * 3 + dash: "V",
                  dash * 2 + dot * 3: "7",
                  dash + dot + dash + dot + dash + dot: ";",
                  dash + dot * 4 + dash: "-",
                  dot * 2 + dash * 2 + dot + dash: "_",
                  dash + dot + dash * 2 + dot + dash: ")",
                  dash + dot + dash + dot + dash * 2: "!",
                  dash * 2 + dot: "G", dash * 2 + dot + dash: "Q",
                  dash * 2 + dot * 2: "Z", dash + dot * 2 + dash + dot: "/",
                  dot + dash + dot + dash + dot: "+",
                  dash + dot + dash + dot: "C", dash * 3 + dot * 3: ":",
                  dash + dot + dash * 2: "Y", dash: "T",
                  dot + dash * 2 + dot + dash + dot: "@",
                  dot * 3 + dash + dot * 2 + dash: "$", dot + dash * 3: "J",
                  dash * 5: "0", dash * 4 + dot: "9",
                  dot + dash + dot * 2 + dash + dot: '"',
                  dash + dot + dash * 2 + dot: "(",
                  dash * 3 + dot * 2: "8",
                  dot * 3 + dash * 2: "3", }

    """writing logs to the console"""
    print(message.from_user.first_name,
          "[", message.from_user.id, "]:", message.text)

    """check if the user wrote something
    other than the first command"""
    if user_Input[0] != "":

        """check which command the user used.
        then we use the method of sending a message
        in which we use the morse method
        to encode or decode the message"""
        match fisrt_command:
            case "/decode":
                user_Input = ' '.join(user_Input)

                print("decoding from morse code\n")
                bot.send_message(message.from_user.id,
                                 Morse.decodeMorse(user_Input, morse_code))
            case "/encode":
                user_Input = ' '.join(user_Input)

                print("encoding from morse code\n")
                bot.send_message(message.from_user.id,
                                 Morse.encodeMorse(user_Input, morse_code))

            case _:
                bot.send_message(message.from_user.id, "Command is incorrect")

        """tell the user to fuck off because he's a moron"""
    else:
        bot.send_message(message.from_user.id,
                         "You cannot encode or decode nothing")


"""we endlessly send requests to the server
to check if the user has written something to us"""

bot.polling(none_stop=True, interval=0)
