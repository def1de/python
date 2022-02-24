#5199685407:AAH2UXVfbWx174bteUGpmYrUT8ZTaipw3mw

import telebot
from telebot import types

bot = telebot.TeleBot("5199685407:AAH2UXVfbWx174bteUGpmYrUT8ZTaipw3mw", parse_mode=None)

name = ''
surname = ''
age = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message,f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
#	bot.reply_to(message, message.text)
	if message.text == 'Привет' or message.text == 'привет':
		bot.reply_to(message, 'Здравствуйте')
	elif message.text == '/reg':
		bot.send_message(message.from_user.id, 'Привет, давай же мы всё таки как-то познакомимся.\nКак тебя зовут?')
		bot.register_next_step_handler(message, register_name)
	else:
		bot.reply_to(message, 'Invalid value')

def register_name(message):
	bot.send_message(message.from_user.id, 'Какая твоя фамилия?')
	global name
	name = message.text
	bot.register_next_step_handler(message, register_surname)

def register_surname(message):
	bot.send_message(message.from_user.id, 'Какой твой возраст?')
	global surname
	surname = message.text
	bot.register_next_step_handler(message, register_age)

def register_age(message):
	global age
	while age == 0:
		try:
			age = int(message.text)
		except Exception: bot.send_message(message.from_user.id, 'Введите цифрами')
	a = f"Тебе {age}, тебя зовут {name.title()} {surname.title()}, верно ли?"
	keyword = types.InlineKeyboardMarkup()
	keyword_yes = types.InlineKeyboardButton(text='YES!', callback_data='yes')
	keyword_no = types.InlineKeyboardButton(text='NOPE!', callback_data='no')
	keyword.add(keyword_yes, keyword_no)
	bot.send_message(message.from_user.id, text=a, reply_markup=keyword)

@bot.callback_query_handler(func=lambda call: True)
def check(call):
	if call.data == 'yes':
		bot.send_message(call.message.chat.id, 'Это здорово. Я внесу тебя в систему.')
	elif call.data == 'no':
		bot.send_message(call.message.chat.id, 'Давай попробуем ещё раз.\nКак тебя зовут?')
		bot.register_next_step_handler(call.message, register_name)

bot.infinity_polling()