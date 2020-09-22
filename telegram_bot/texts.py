from telegram_bot.utils.utils_market import value_orders_date
from telegram_bot.utils.utils_bb import find_registered_users, corrected_users_id,\
    sorted_masters_and_salon, add_roles, users_who_created_bids


def reports_yesterday(date):
    value, count = value_orders_date(date, date)
    return f"За {date}: "\
           f"продаж - {count}; "\
           f"сумма продаж - {value}."


def reports_registration_bb(start_date, end_date):
    registrations = find_registered_users(start_date, end_date)
    correct_id = corrected_users_id(registrations)
    add_roles(correct_id)
    sorted = sorted_masters_and_salon(correct_id)
    return f"Зарегистрировано за период {start_date}/{end_date}:" \
           f"{sorted}." \
           f"Всего регистраций: {len(registrations)}"


def reports_active_users(start_date, end_date):
    count_bids, active_users = users_who_created_bids(start_date, end_date)
    correct_return = []
    for user in active_users:
        if user.get('bids') > 1:
            correct_return.append((user.get('user_id'),user.get('name'), user.get('bids')))
    return f"За период {start_date}/{end_date}: " \
           f"Создано заявок {count_bids}. " \
           f"Пользователей создавали заявки {len(active_users)}. " \
           f"Больше 1 заявки у {[i for i in correct_return]}"
