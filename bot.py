import telebot 
from telebot import types
import random
from bot_logic import gen_pass, d4, d6, d8, d10, d12, d20, d100


bot = telebot.TeleBot("8486010197:AAGZvakHyGKlj4naANlKsLu3D4Tor66V6ug")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"""Salve magister. Я есть бот {bot.get_me().first_name}. Мои комманды: \n/gen_pass - Создаю пароль из 7 символов \n/dice - ассортимент кубиков""")

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "хи" * count_heh)


@bot.message_handler(commands=['gen_pass'])
def send_pass(message):
    bot.reply_to(message, gen_pass(7))




@bot.message_handler(commands=['dice'])
@bot.message_handler(commands =['button'])
def button(message):
    dices = types.InlineKeyboardMarkup(row_width=2)
    cube1 = types.InlineKeyboardButton('d4', callback_data='cube1')
    cube2 = types.InlineKeyboardButton('d6', callback_data='cube2')
    cube3 = types.InlineKeyboardButton('d8', callback_data='cube3')
    cube4 = types.InlineKeyboardButton('d10', callback_data='cube4')
    cube5 = types.InlineKeyboardButton('d12', callback_data='cube5')
    cube6 = types.InlineKeyboardButton('d20', callback_data='cube6')
    cube7 = types.InlineKeyboardButton('d100', callback_data='cube7')
    dices.add(cube1, cube2, cube3, cube4, cube5, cube6, cube7)

    bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text='The dice list!!!', reply_markup=dices)
    

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'cube1':
            bot.send_message(call.message.chat.id, d4())
        elif call.data == 'cube2':
            bot.send_message(call.message.chat.id, d6())
        elif call.data == 'cube3':
            bot.send_message(call.message.chat.id, d8())
        elif call.data == 'cube4':
            bot.send_message(call.message.chat.id, d10())
        elif call.data == 'cube5':
            bot.send_message(call.message.chat.id, d12())
        elif call.data == 'cube6':
            bot.send_message(call.message.chat.id, d20())
        elif call.data == 'cube7':
            bot.send_message(call.message.chat.id, d100())


@bot.message_handler(commands=['roll'])
def send_pass(message):
    side = int(message.text.split()[1])
    bot.reply_to(message, random.randint(1, side))




@bot.message_handler(commands=['d4'])
def send_pass(message):
    bot.reply_to(message, d4())


@bot.message_handler(commands=['d6'])
def send_pass(message):
    bot.reply_to(message, d6())

@bot.message_handler(commands=['d8'])
def send_pass(message):
    bot.reply_to(message, d8())

@bot.message_handler(commands=['d10'])
def send_pass(message):
    bot.reply_to(message, d10())

@bot.message_handler(commands=['d12'])
def send_pass(message):
    bot.reply_to(message, d12())

@bot.message_handler(commands=['d20'])
def send_pass(message):
    bot.reply_to(message, d20())

@bot.message_handler(commands=['d100'])
def send_pass(message):
    bot.reply_to(message, d100())



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.infinity_polling()
