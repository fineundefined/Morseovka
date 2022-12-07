"""
This is main file.

This is where message processing takes place,
encoding and decoding functions are called,
and messages are sent.
"""
import os
from Morse import Morse
import telebot
from audiomorse import morse_to_wav
import random

"""set bot token"""
bot = telebot.TeleBot('')

"""main function start"""
if __name__ == "__main__":
    m = Morse()
    """set console name"""
    os.system("title Morseovka")

"""set the list of bot commands"""
bot.set_my_commands([
    telebot.types.BotCommand("/help",
                             "/help to get commands list"),
    telebot.types.BotCommand("/encode",
                             "/encode + text + &%dot% -&%dash% — (optional)"),
    telebot.types.BotCommand("/decode",
                             "/decode + morse code + "
                             "-&%dot% -&%dash% — (optional)")
])


"""new user message processing function"""


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """
    This function captures the user's messages. Processes them and sends a response.
    """
    print(message.from_user.id)
    """Add message text to variable."""
    user_input = message.text
    """create a list from the text of the
    message with the separator " " with maximum separation 1"""
    user_input = user_input.split(" ", 1)

    """add the first command to the variable"""
    first_command = user_input[0]
    """remove the first command from the list"""
    del user_input[0]

    """create a string from a list"""
    user_input = ''.join(user_input)

    """we are trying to split the string again
    and set the values of the dot and dash
    to those that the user sent in the message"""

    user_input = user_input.split(' &', 2)
    if len(user_input) == 3:
        dot = user_input[1]
        dash = user_input[2]
        m.set_morse(dot, dash)
        del user_input[1:3]
    else:
        m.set_morse()

    """writing logs to the console"""
    print(message.from_user.first_name,
          "[", message.from_user.id, "]:", message.text)
    """check if the user wrote something
    other than the first command"""
    if user_input[0] != "":
        user_input = ' '.join(user_input)
        """check which command the user used.
        then we use the method of sending a message
        in which we use the morse method
        to encode or decode the message"""
        match first_command:
            case "/decode":

                try:
                    bot.send_message(message.from_user.id,
                                     Morse.decodeMorse(user_input,
                                                       m.morse_code))

                    print("decoded from morse code\n")

                except:  # noqa: E722
                    bot.send_message(message.from_user.id,
                                     "ERROR")
                    raise ("ERROR")

            case "/encode":
                try:
                    bot.send_message(message.from_user.id,
                                     Morse.encodeMorse(user_input,
                                                       m.morse_code))

                    print("encoded from morse code\n")

                except:  # noqa: E722
                    bot.send_message(message.from_user.id,
                                     "ERROR")
                    raise ("ERROR")

            case "/eaudio":
                if len(user_input) <= 30:
                    print("encoded from morse code\n")
                    rn = random.randrange(0, 100)
                    print(rn)
                    newpath = "C:\\Users\\A\\PycharmProjects" \
                              "\\telebotPY\\newfile",\
                              str(rn), ".mp3"
                    pathjoin = ''.join(newpath)
                    newfile = open(pathjoin, 'x')
                    newfile.close()

                    morse_to_wav(Morse.encodeMorse(user_input,
                                                   m.morse_code), pathjoin)

                    bot.send_audio(message.from_user.id,
                                   open(pathjoin, 'rb'),
                                   title="Morse",
                                   caption="@morseovka_bot")
                    os.remove(pathjoin)
                else:
                    bot.send_message(message.from_user.id,
                                     "Message must be less then 20 symbols")

            case _:
                bot.send_message(message.from_user.id,
                                 "There is no command in the message."
                                 " Write /help to get commands list")

    elif user_input[0] == "":
        """if there is no text in the message and
        the first command matches the list,
        send the message"""
        if first_command in ["/help", "/start"]:
            bot.send_message(message.from_user.id,
                             '/decode + "text '
                             'to decode from format "-.-." or'
                             ' use parameters '
                             'to change value of dot and dash symbol"'
                             ' &dot parameter &dash parameter \n'
                             '/encode + "text '
                             'to encode to format "-.-." or'
                             ' use parameters '
                             'to change value of dot and dash symbol"'
                             ' &dot parameter &dash parameter')
        elif first_command in ["/decode", "/encode"]:
            bot.send_message(message.from_user.id, "decode/encode + "
                                                   "text + dotParam + "
                                                   "dashParam(Parameters "
                                                   "should start with '&')")
        else:
            bot.send_message(message.from_user.id, "There is no "
                                                   "command in the message."
                                                   " Write /help "
                                                   "to get commands list")


"""we endlessly send requests to the server
to check if the user has written something to us"""

bot.polling(none_stop=True, interval=0)
