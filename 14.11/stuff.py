import telebot
token = '1051164578:AAHy1AM7SAWCQ7yo4WRasqki9fpwB4cI-wU'


bot = telebot.TeleBot(token)

print(bot)

@bot.message_handler(commands=['start', 'Price'])
def guess_message(message):
    print(message.text)
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    itembtna = telebot.types.KeyboardButton('Price')
    itembtnv = telebot.types.KeyboardButton('v')
    itembtnc = telebot.types.KeyboardButton('c')
    itembtnd = telebot.types.KeyboardButton('d')
    itembtne = telebot.types.KeyboardButton('Help')
    keyboard.row(itembtna, itembtnv)
    keyboard.row(itembtnc, itembtnd, itembtne)
    msg = bot.send_message(message.chat.id, "Hello", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Price')
def echo_all(message):
    print(message)
    bot.send_message(message.chat.id, 'Just write the name of the asset')



@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.send_message(message.chat.id, "I'm sorry but I do not understand you")


bot.polling()