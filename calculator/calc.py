import telebot
import ler
from fractions import Fraction
from telebot import types

bot = telebot.TeleBot(ler.token)


@bot.message_handler(commands=['start'])
def button_1(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*[types.KeyboardButton(name) for name in ['Rational numbers', 'Complex numbers']])
    bot.send_message(message.chat.id, "Hi, I'm a calculator bot.\nPlease, select category.", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Rational numbers':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add(*[types.KeyboardButton(name) for name in ['Addition', 'Subtraction', 'Multiplication', 'Division']])
        bot.send_message(message.chat.id, "Select operation", reply_markup=markup)
    elif message.text == 'Addition':
        mes = bot.send_message(message.chat.id, 'Enter numerator of the first fraction:')
        bot.register_next_step_handler(mes, handle_text)
    elif message.text == 'Subtraction':
        mes = bot.send_message(message.chat.id, 'Enter numerator of the first fraction:')
        bot.register_next_step_handler(mes, handle_text_1)
    elif message.text == 'Multiplication':
        mes = bot.send_message(message.chat.id, 'Enter numerator of the first fraction:')
        bot.register_next_step_handler(mes, handle_text_2)
    elif message.text == 'Division':
        mes = bot.send_message(message.chat.id, 'Enter numerator of the first fraction:')
        bot.register_next_step_handler(mes, handle_text_3)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add(*[types.KeyboardButton(name) for name in ['addition', 'subtraction', 'multiplication', 'division']])
        bot.send_message(message.chat.id, "Select operation", reply_markup=markup)
    if message.text == 'addition':
        mes = bot.send_message(message.chat.id, 'Enter first coefficient for the first number:')
        bot.register_next_step_handler(mes, handle_text_4)
    elif message.text == 'subtraction':
        mes = bot.send_message(message.chat.id, 'Enter first coefficient for the first number:')
        bot.register_next_step_handler(mes, handle_text_5)
    elif message.text == 'multiplication':
        mes = bot.send_message(message.chat.id, 'Enter first coefficient for the first number:')
        bot.register_next_step_handler(mes, handle_text_6)
    elif message.text == 'division':
        mes = bot.send_message(message.chat.id, 'Enter first coefficient for the first number:')
        bot.register_next_step_handler(mes, handle_text_7)


@bot.message_handler()
def handle_text(message):
    global numer_1
    numer_1 = message.text
    mes_1 = bot.send_message(message.chat.id, 'Enter denominator of the first fraction:')
    bot.register_next_step_handler(mes_1, num_fun)


def num_fun(message):
    global denom_1
    denom_1 = message.text
    mes_2 = bot.send_message(message.chat.id, 'Enter numerator of the second fraction:')
    bot.register_next_step_handler(mes_2, num_1_fun)


def num_1_fun(message):
    global numer_2
    numer_2 = message.text
    num_2 = bot.send_message(message.chat.id, 'Enter denominator of the second fraction:')
    bot.register_next_step_handler(num_2, operation_ad)


def operation_ad(message):
    global denom_2
    denom_2 = message.text
    result = Fraction(int(numer_1), int(denom_1)) + Fraction(int(numer_2), int(denom_2))
    bot.send_message(message.chat.id, f'{result}')


@bot.message_handler()
def handle_text_1(message):
    global numer_1
    numer_1 = message.text
    mes_1 = bot.send_message(message.chat.id, 'Enter denominator of the first fraction:')
    bot.register_next_step_handler(mes_1, num_fu)


def num_fu(message):
    global denom_1
    denom_1 = message.text
    mes_2 = bot.send_message(message.chat.id, 'Enter numerator of the second fraction:')
    bot.register_next_step_handler(mes_2, num_1_fu)


def num_1_fu(message):
    global numer_2
    numer_2 = message.text
    num_2 = bot.send_message(message.chat.id, 'Enter denominator of the second fraction:')
    bot.register_next_step_handler(num_2, operation_sub)


def operation_sub(message):
    global denom_2
    denom_2 = message.text
    result = Fraction(int(numer_1), int(denom_1)) - Fraction(int(numer_2), int(denom_2))
    bot.send_message(message.chat.id, f'{result}')


@bot.message_handler()
def handle_text_2(message):
    global numer_1
    numer_1 = message.text
    mes_1 = bot.send_message(message.chat.id, 'Enter denominator of the first fraction:')
    bot.register_next_step_handler(mes_1, num_f)


def num_f(message):
    global denom_1
    denom_1 = message.text
    mes_2 = bot.send_message(message.chat.id, 'Enter numerator of the second fraction:')
    bot.register_next_step_handler(mes_2, num_1_f)


def num_1_f(message):
    global numer_2
    numer_2 = message.text
    num_2 = bot.send_message(message.chat.id, 'Enter denominator of the second fraction:')
    bot.register_next_step_handler(num_2, operation_mult)


def operation_mult(message):
    global denom_2
    denom_2 = message.text
    result = Fraction(int(numer_1), int(denom_1)) * Fraction(int(numer_2), int(denom_2))
    bot.send_message(message.chat.id, f'{result}')


@bot.message_handler()
def handle_text_3(message):
    global numer_1
    numer_1 = message.text
    mes_1 = bot.send_message(message.chat.id, 'Enter denominator of the first fraction:')
    bot.register_next_step_handler(mes_1, num_func)


def num_func(message):
    global denom_1
    denom_1 = message.text
    mes_2 = bot.send_message(message.chat.id, 'Enter numerator of the second fraction:')
    bot.register_next_step_handler(mes_2, num_2_f)


def num_2_f(message):
    global numer_2
    numer_2 = message.text
    num_2 = bot.send_message(message.chat.id, 'Enter denominator of the second fraction:')
    bot.register_next_step_handler(num_2, operation_division)


def operation_division(message):
    global denom_2
    denom_2 = message.text
    result = Fraction(int(numer_1), int(denom_1)) / Fraction(int(numer_2), int(denom_2))
    bot.send_message(message.chat.id, f'{result}')


@bot.message_handler()
def handle_text_4(message):
    global numer_1
    numer_1 = message.text
    mes_1 = bot.send_message(message.chat.id, 'Enter second coefficient for the first number:')
    bot.register_next_step_handler(mes_1, num_func_3)


def num_func_3(message):
    global denom_1
    denom_1 = message.text
    mes_2 = bot.send_message(message.chat.id, 'Enter first coefficient for the second number:')
    bot.register_next_step_handler(mes_2, num_3_f)


def num_3_f(message):
    global numer_2
    numer_2 = message.text
    num_2 = bot.send_message(message.chat.id, 'Enter second coefficient for the second number:')
    bot.register_next_step_handler(num_2, operat_sum)


def operat_sum(message):
    global denom_2
    denom_2 = message.text
    result = complex(int(numer_1), int(denom_1)) + complex(int(numer_2), int(denom_2))
    bot.send_message(message.chat.id, f'{result}')


@bot.message_handler()
def handle_text_5(message):
    global numer_1
    numer_1 = message.text
    mes_1 = bot.send_message(message.chat.id, 'Enter second coefficient for the first number:')
    bot.register_next_step_handler(mes_1, num_func_4)


def num_func_4(message):
    global denom_1
    denom_1 = message.text
    mes_2 = bot.send_message(message.chat.id, 'Enter first coefficient for the second number:')
    bot.register_next_step_handler(mes_2, num_4_f)


def num_4_f(message):
    global numer_2
    numer_2 = message.text
    num_2 = bot.send_message(message.chat.id, 'Enter second coefficient for the second number:')
    bot.register_next_step_handler(num_2, operat_sub)


def operat_sub(message):
    global denom_2
    denom_2 = message.text
    result = complex(int(numer_1), int(denom_1)) - complex(int(numer_2), int(denom_2))
    bot.send_message(message.chat.id, f'{result}')


@bot.message_handler()
def handle_text_6(message):
    global numer_1
    numer_1 = message.text
    mes_1 = bot.send_message(message.chat.id, 'Enter second coefficient for the first number:')
    bot.register_next_step_handler(mes_1, num_func_5)


def num_func_5(message):
    global denom_1
    denom_1 = message.text
    mes_2 = bot.send_message(message.chat.id, 'Enter first coefficient for the second number:')
    bot.register_next_step_handler(mes_2, num_5_f)


def num_5_f(message):
    global numer_2
    numer_2 = message.text
    num_2 = bot.send_message(message.chat.id, 'Enter second coefficient for the second number:')
    bot.register_next_step_handler(num_2, operat_mult)


def operat_mult(message):
    global denom_2
    denom_2 = message.text
    result = complex(int(numer_1), int(denom_1)) * complex(int(numer_2), int(denom_2))
    bot.send_message(message.chat.id, f'{result}')


@bot.message_handler()
def handle_text_7(message):
    global numer_1
    numer_1 = message.text
    mes_1 = bot.send_message(message.chat.id, 'Enter second coefficient for the first number:')
    bot.register_next_step_handler(mes_1, num_func_7)


def num_func_7(message):
    global denom_1
    denom_1 = message.text
    mes_2 = bot.send_message(message.chat.id, 'Enter first coefficient for the second number:')
    bot.register_next_step_handler(mes_2, num_6_f)


def num_6_f(message):
    global numer_2
    numer_2 = message.text
    num_2 = bot.send_message(message.chat.id, 'Enter second coefficient for the second number:')
    bot.register_next_step_handler(num_2, operat_div)


def operat_div(message):
    global denom_2
    denom_2 = message.text
    result = complex(int(numer_1), int(denom_1)) / complex(int(numer_2), int(denom_2))
    bot.send_message(message.chat.id, f'{result}')


if __name__ == '__main__':
    bot.polling(none_stop=True)
