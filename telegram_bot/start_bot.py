# https://github.com/eternnoir/pyTelegramBotAPI#more-examples
import os
import telebot
from telebot import types
from dotenv import load_dotenv
from telegram_bot.utils.utils import get_dates
from telegram_bot.texts import reports_yesterday, reports_registration_bb, reports_active_users
load_dotenv()


token = os.getenv('secret_token')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Введите пароль, для доступа к аналитике')


@bot.message_handler(regexp="1432")
def start_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Beauty box')
    itembtn2 = types.KeyboardButton(f'Beauty market')
    markup.add(itembtn1, itembtn2)
    bot.reply_to(message, 'Выберите проект', reply_markup=markup)


@bot.message_handler(regexp="На главную")
def home(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Beauty box')
    itembtn2 = types.KeyboardButton(f'Beauty market')
    markup.add(itembtn1, itembtn2)
    bot.reply_to(message, 'Выберите проект', reply_markup=markup)


@bot.message_handler(regexp="Beauty market")
def beauty_market_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Продажи')
    itembtn2 = types.KeyboardButton(f'Возвращаемость')
    itembtn3 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp="Beauty box")
def beauty_box_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Регистрации')
    itembtn2 = types.KeyboardButton(f'Активные пользователи')
    itembtn3 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp="Продажи")
def beautymarket_orders(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Интернет за {get_dates()[0]}')  # yesterday
    itembtn2 = types.KeyboardButton(f'Интернет за {get_dates()[1]}')
    itembtn3 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp="Регистрации")
def beauty_box_reports(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f"Зарегистрировались за {get_dates()[0]}")  # yesterday
    itembtn2 = types.KeyboardButton(f"Зарегистрировались за {get_dates()[1]}")
    itembtn3 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp="Активные пользователи")
def beauty_box_reports(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f"Активные за {get_dates()[0]}")
    itembtn2 = types.KeyboardButton(f"Активные за {get_dates()[1]}")
    itembtn3 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp=f"Активные за {get_dates()[0]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, f"{reports_active_users(get_dates()[2], get_dates()[2])}")  # yesterday, yesterday


@bot.message_handler(regexp=f"Активные за {get_dates()[1]}")  # today
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, f"{reports_active_users(get_dates()[3], get_dates()[3])}")  # today, today


@bot.message_handler(regexp=f"Зарегистрировались за {get_dates()[0]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, f"{reports_registration_bb(get_dates()[2], get_dates()[2])}")


@bot.message_handler(regexp=f"Зарегистрировались за {get_dates()[1]}")
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, f"{reports_registration_bb(get_dates()[3], get_dates()[3])}")  # today, today


@bot.message_handler(regexp=f"Интернет за {get_dates()[0]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, f"{reports_yesterday(get_dates()[2])}")


@bot.message_handler(regexp=f"Интернет за {get_dates()[1]}")
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, f"{reports_yesterday(get_dates()[3])}")


def start():
    bot.polling(timeout=1000)


if __name__ == '__main__':
    start()
