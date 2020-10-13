# https://github.com/eternnoir/pyTelegramBotAPI#more-examples
import os
from time import sleep
from datetime import datetime
from django.db import connection
import django
import telebot
from telebot import types
from dotenv import load_dotenv
from telegram_bot.utils.utils import get_dates
from telegram_bot.texts import reports_yesterday, reports_registration_bb, reports_active_users, \
    reports_moysclad
from django.db.utils import OperationalError
load_dotenv()


token = os.getenv('secret_token_test')
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
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton(f'Интернет')  # yesterday
    itembtn2 = types.KeyboardButton(f'Москва')
    itembtn3 = types.KeyboardButton(f'Саратов')
    itembtn4 = types.KeyboardButton(f'Балаково')
    itembtn5 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)

#
# @bot.message_handler(regexp="Интернет")
# def beautymarket_orders(message):
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton(f'Интернет за {get_dates()[0]}')  # yesterday
#     itembtn2 = types.KeyboardButton(f'Интернет за {get_dates()[1]}')
#     itembtn3 = types.KeyboardButton(f'На главную')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


# @bot.message_handler(regexp=f"Интернет за {get_dates()[0]}")  # yesterday
# def handle_message(message):
#     markup = types.ReplyKeyboardMarkup()
#     itembtn1 = types.KeyboardButton('На главную')
#     markup.add(itembtn1)
#     bot.reply_to(message, f"{reports_yesterday(get_dates()[2])}")


# @bot.message_handler(regexp=f"Интернет за {get_dates()[1]}")
# def handle_message(message):
#     markup = types.ReplyKeyboardMarkup()
#     itembtn1 = types.KeyboardButton('На главную')
#     markup.add(itembtn1)
#     bot.reply_to(message, f"{reports_yesterday(get_dates()[3])}")


@bot.message_handler(regexp="Москва")
def beautymarket_orders_msc(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Msk {get_dates()[0]}')  # yesterday
    itembtn2 = types.KeyboardButton(f'Msk {get_dates()[1]}')
    itembtn3 = types.KeyboardButton(f'Продажи')
    itembtn4 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp="Саратов")
def beautymarket_orders_msc(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Saratov {get_dates()[0]}')  # yesterday
    itembtn2 = types.KeyboardButton(f'Saratov {get_dates()[1]}')
    itembtn3 = types.KeyboardButton(f'Продажи')
    itembtn4 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp=f"Saratov {get_dates()[0]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Продажи')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    _, quantity, sum = reports_moysclad(get_dates()[2], get_dates()[2], 'saratov')  # today, today
    bot.reply_to(message, f"За период {get_dates()[0]}/{get_dates()[0]}: \n"
                          f"со склада 'Саратов' \n"
                          f"продаж {quantity} \n"
                          f"на сумму {sum} тыс.", reply_markup=markup)


@bot.message_handler(regexp=f"Saratov {get_dates()[1]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Продажи')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    _, quantity, sum = reports_moysclad(get_dates()[3], get_dates()[3], 'saratov')  # today, today
    bot.reply_to(message, f"За период {get_dates()[1]}/{get_dates()[1]}: \n"
                          f"со склада 'Саратов' \n"
                          f"продаж {quantity} \n"
                          f"на сумму {sum} тыс.", reply_markup=markup)


@bot.message_handler(regexp="Интернет")
def beautymarket_orders_msc(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Internet {get_dates()[0]}')  # yesterday
    itembtn2 = types.KeyboardButton(f'Internet {get_dates()[1]}')
    itembtn3 = types.KeyboardButton(f'Продажи')
    itembtn4 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp=f"Internet {get_dates()[0]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Продажи')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    _, quantity, sum = reports_moysclad(get_dates()[2], get_dates()[2], 'internet')  # today, today
    bot.reply_to(message, f"За период {get_dates()[0]}/{get_dates()[0]}: \n"
                          f"со склада 'Интернет' \n"
                          f"продаж {quantity} \n"
                          f"на сумму {sum} тыс.", reply_markup=markup)


@bot.message_handler(regexp=f"Internet {get_dates()[1]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Продажи')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    _, quantity, sum = reports_moysclad(get_dates()[3], get_dates()[3], 'internet')  # today, today
    bot.reply_to(message, f"За период {get_dates()[1]}/{get_dates()[1]}: \n"
                          f"со склада 'Интернет' \n"
                          f"продаж {quantity} \n"
                          f"на сумму {sum} тыс.", reply_markup=markup)


@bot.message_handler(regexp="Балаково")
def beautymarket_orders_msc(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton(f'Balakovo {get_dates()[0]}')  # yesterday
    itembtn2 = types.KeyboardButton(f'Balakovo {get_dates()[1]}')
    itembtn3 = types.KeyboardButton(f'Продажи')
    itembtn4 = types.KeyboardButton(f'На главную')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.reply_to(message, 'Выберите интересующий отчет', reply_markup=markup)


@bot.message_handler(regexp=f"Balakovo {get_dates()[0]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Продажи')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    _, quantity, sum = reports_moysclad(get_dates()[2], get_dates()[2], 'green_house')  # today, today
    bot.reply_to(message, f"За период {get_dates()[0]}/{get_dates()[0]}: \n"
                          f"со склада 'Балаково' \n"
                          f"продаж {quantity} \n"
                          f"на сумму {sum} тыс.", reply_markup=markup)


@bot.message_handler(regexp=f"Balakovo {get_dates()[1]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Продажи')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    _, quantity, sum = reports_moysclad(get_dates()[3], get_dates()[3], 'green_house')  # today, today
    bot.reply_to(message, f"За период {get_dates()[1]}/{get_dates()[1]}: \n"
                          f"со склада 'Балаково' \n"
                          f"продаж {quantity} \n"
                          f"на сумму {sum} тыс.", reply_markup=markup)


@bot.message_handler(regexp=f"Msk {get_dates()[0]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Продажи')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    _, quantity, sum = reports_moysclad(get_dates()[2], get_dates()[2], 'moscow_store')  # today, today
    bot.reply_to(message, f"За период {get_dates()[0]}/{get_dates()[0]}: \n"
                          f"со склада 'Москва' \n"
                          f"продаж {quantity} \n"
                          f"на сумму {sum} тыс.", reply_markup=markup)


@bot.message_handler(regexp=f"Msk {get_dates()[1]}")  # yesterday
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Продажи')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    _, quantity, sum = reports_moysclad(get_dates()[3], get_dates()[3], 'moscow_store')  # today, today
    bot.reply_to(message, f"За период {get_dates()[1]}/{get_dates()[1]}: \n"
                          f"со склада 'Москва' \n"
                          f"продаж {quantity} \n"
                          f"на сумму {sum} тыс.", reply_markup=markup)


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
    time, bids, active_users, activ_list = reports_active_users(get_dates()[2], get_dates()[2])  # today, today
    bot.reply_to(message, f"{time} \n"
                          f"{bids} \n"
                          f"{active_users} \n"
                          f"{activ_list}")

@bot.message_handler(regexp=f"Активные за {get_dates()[1]}")  # today
def handle_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    time, bids, active_users, activ_list = reports_active_users(get_dates()[3], get_dates()[3])  # today, today
    bot.reply_to(message, f"{time} \n"
                          f"{bids} \n"
                          f"{active_users} \n"
                          f"{activ_list}")


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


def start():
    while True:
        try:
            bot.polling(timeout=1000)
        except OperationalError:
            db_conn = None
            while not db_conn:
                try:
                    connection.ensure_connection()
                    db_conn = True
                except OperationalError:
                    print('Database unavailable, waiting 1 second...')
                    sleep(5)
            print('Database available!')
        except Exception as e:
            print(datetime.now())
            print(e)
            sleep(5)
            bot.polling(timeout=1000)


if __name__ == '__main__':
    start()
