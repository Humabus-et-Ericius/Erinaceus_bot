import telebot 
from bot_logic import gen_pass, d4, d6, d8, d10, d12, d20, d100
bot = telebot.TeleBot("8486010197:AAGZvakHyGKlj4naANlKsLu3D4Tor66V6ug")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """Salve magister. Я есть бот Тихона. Мои комманды: \n/gen_pass - Создаю пароль из 7 символов \n/d4 - кидаю 4х - гранный кубик"""
                 """\n/d6 - кидаю 6ти-гранный кубик\n/d8 - кидаю 8ми-гранный кубик \n/d10 - кидаю 10ти-гранный кубик \n/d20 - кидаю 20ти-гранный кубик \n/d100 - кидаю 100 - гранный кубик  """)

@bot.message_handler(commands=['gen_pass'])
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
