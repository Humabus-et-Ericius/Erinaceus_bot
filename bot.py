import telebot
from bot_logic import gen_pass, d4



bot = telebot.TeleBot("8486010197:AAGZvakHyGKlj4naANlKsLu3D4Tor66V6ug")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salve magister")

@bot.message_handler(commands=['gimme_passwrd'])
def send_pass(message):
    bot.reply_to(message, gen_pass(7))

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

bot.polling()
