import os
from Morse import *
from GetFile import *
from TeamName import *
import telebot

#set bot token
bot = telebot.TeleBot('5696255478:AAFOUU4s1jost8eK31jyzZv4BkdZDZBJ-Wc')

#main function start
if __name__ == "__main__":
    #set console name
    os.system("title Morseovka")
    #set console size
    os.system("mode con cols=101 lines=30")
#set the list of bot commands
bot.set_my_commands([
    telebot.types.BotCommand("/encode", "'/encode + text'"),
    telebot.types.BotCommand("/decode", "/decode + morse code")
])


#new user message processing function
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    #add message text to variable
    user_Input = message.text
    #create a list from the text of the message with the separator " " with maximum separation 1
    user_Input = user_Input.split(" ", 1)
    #add the first command to the variable
    fisrt_command = user_Input[0]
    #remove the first command from the list
    del user_Input[0]
    #create a string from a list
    user_Input = ''.join(user_Input)
    #set the default dot value(then I'll change it)
    dot = '.'
    #set the default dash value
    dash = '-'
    #we are trying to split the string again and set the values of the dot and dash to those that the user sent in the message
    try:
        user_Input = user_Input.split(' /', 2)
        dot = user_Input[1]
        dash = user_Input[2]
        del user_Input[1:3]
    #if there were no values in the message, then skip this step
    except:
        pass

    #writing logs to the console
    print(message.from_user.first_name, "[", message.from_user.id, "]:", message.text)
    #check if the user wrote something other than the first command
    if user_Input[0] != "":
        #check which command the user used. then we use the method of sending a message in which we use the morse method to encode or decode the message
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
    #tell the user to fuck off because he's a moron
    else:
        bot.send_message(message.from_user.id, "You cannot encode or decode nothing")

#we endlessly send requests to the server to check if the user has written something to us
bot.polling(none_stop=True, interval=0)
