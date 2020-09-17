from datetime import datetime, timedelta


def get_dates():
    date_format = '%d.%m.%Y'
    date_format_bd = '%Y-%m-%d'
    today = datetime.now()
    yesterday = today + timedelta(days=-1)
    return yesterday.strftime(date_format), today.strftime(date_format),\
           yesterday.strftime(date_format_bd), today.strftime(date_format_bd)


def date_func():
    yesterday, today, yesterday_db, today_db = get_dates()
    return yesterday, today, yesterday_db, today_db
