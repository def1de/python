import telebot
from telebot import types

bot = telebot.TeleBot("5199685407:AAH2UXVfbWx174bteUGpmYrUT8ZTaipw3mw", parse_mode=None)

name = ''

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.from_user.id, f'Здравствуйте напишите /reg для регистрации')

@bot.message_handler(commands=['reg'])
def register(message):
    name = message.from_user.first_name
    a = f'Ваше имя {name}?'
    keyword = telebot.types.InlineKeyboardMarkup()
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
		bot.register_next_step_handler(call.message, register)

bot.infinity_polling()
