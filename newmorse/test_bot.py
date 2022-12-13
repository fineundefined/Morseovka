import telebot
from Morse import Morse
import time

bot = telebot.TeleBot('BOT_TOKEN')


@bot.message_handler(commands=['test'])
def get_command(message):
    start_time = time.time()
    user_id = CHAT_ID
    if message.from_user.id == user_id:
        user_input = message.text
        user_input = user_input.split(' /')
        del user_input[0]
        if len(user_input) < 30:
            bot_send(user_input, user_id, start_time)
        else:
            bot.send_message(user_id, 'Too many tests')
    else:
        bot.send_message(user_id, 'you have no permissions')


@bot.message_handler(commands=['auto'])
def autotest(message):
    if message.from_user.id == CHAT_ID:
        test_send()


def bot_send(user_input, user_id, start_time):
    m = Morse()
    success = u'\U00002705'
    failed = u'\U0000274C'
    doublemark = u'\U0000203C'
    row = u'\U000027A1'
    success_list = []
    n = 0
    total_success_tests = 0
    failed_tests = []
    total_tests = len(user_input)
    print(start_time)
    for i in user_input:
        n = n + 1
        try:

            encoded = Morse.encodeMorse(i, m.set_morse())
            decoded = Morse.decodeMorse(encoded, m.set_morse())
            if decoded == i and decoded is not None:
                answer = f'{"=" * 25}\n{success} TEST[{n}]:' \
                         f' SUCCESS  with decoding and encoding \nGOT' \
                         f' "{i}"\nencoded to' \
                         f' "{encoded}"\nafter decoding back GOT:' \
                         f' "{decoded}" \n\n"{decoded}" {row} "{i}" \n{"=" * 25}'
                total_success_tests += 1
            elif decoded is None or decoded == ' ':
                answer = f'{"=" * 25}\n{failed} TEST[{n}]: Connot read this' \
                         f' type of message ({i})\n{"=" * 25}'
                failed_tests.append(f'TEST[{n}]')
            else:
                answer = f'{"=" * 25}\n{failed} TEST[{n}]:' \
                         f' FAILED with decoding or encoding \nGOT' \
                         f' "{i}"\nencoded to' \
                         f' "{encoded}"\nafter decoding back GOT:' \
                         f' "{decoded}" \n\n"{decoded}" {doublemark} "{i}" \n{"=" * 25}'
                failed_tests.append(f'TEST[{n}]')
            success_list.append(answer)

        except: # noqa E722
            success_list.append(f'Unknown error with [{i}]')

    failed_tests = '\n     '.join(failed_tests)
    succes_list = '\n\n'.join(success_list)
    final_message = f'{succes_list}' \
                    f' \n\nTotal success tests' \
                    f' {str(total_success_tests)}' \
                    f' \nTotal tests {str(total_tests)}' \
                    f' \n\nFailed Tests List:\n' \
                    f'     {failed_tests}'
    bot.send_message(user_id, f'{final_message}'
                              f' \n[{(time.time() - start_time)}'
                              f' seconds]')
    if total_tests != 0:
        get_procent = (total_success_tests / total_tests) * 100
    else:
        get_procent = 0
    bot.send_message(user_id, f'total test success {get_procent}')
    if get_procent >= 66:
        return True
    else:
        return False


def test_send():
    newlist = ['newtest',
               '     ',
               '123',
               '/""[][][//??>.<@#%^&**()+_=!',
               'qqqqqqqqqqqqqqqqqqqqqqqqqqqqq',
               'hi there']
    assert bot_send(newlist, CHAT_ID, time.time())


bot.polling()
