# https://github.com/eternnoir/pyTelegramBotAPI#more-examples
import os
import telebot
from telebot import types
from dotenv import load_dotenv
from telegram_bot.utils.utils import date_func, get_dates
from telegram_bot.texts import reports_yesterday
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
def beautymarket_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Продажи')
    itembtn2 = types.KeyboardButton(f'Возвращаемость')
    itembtn3 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp="Продажи")
def beautymarket_orders(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Интернет за {date_func()[0]}')
    itembtn2 = types.KeyboardButton(f'Интернет за {date_func()[1]}')
    itembtn3 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp=f"Интернет за {get_dates()[0]}")
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, f"{reports_yesterday(date_func()[2])}")


@bot.message_handler(regexp=f"Интернет за {get_dates()[1]}")
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, f"{reports_yesterday(date_func()[3])}")


def start():
    bot.polling(timeout=1000)


if __name__ == '__main__':
    start()
