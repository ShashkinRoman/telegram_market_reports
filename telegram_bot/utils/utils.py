from datetime import datetime, timedelta


def get_dates():
    date_format = '%d.%m.%Y'
    date_format_bd = '%Y-%m-%d'
    today = datetime.now()
    yesterday = today + timedelta(days=-1)
    tomorrow = today + timedelta(days=+1)
    return yesterday.strftime(date_format), today.strftime(date_format),\
           yesterday.strftime(date_format_bd), today.strftime(date_format_bd), \
           tomorrow.strftime(date_format), tomorrow.strftime(date_format_bd)
