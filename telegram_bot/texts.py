from telegram_bot.utils.utils_market import value_orders_date


def reports_yesterday(date):
    value, count = value_orders_date(date, date)
    return f"За {date}: "\
           f"продаж - {count}; "\
           f"сумма продаж - {value}."
