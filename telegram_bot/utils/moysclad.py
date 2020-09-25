import os
import requests
from dotenv import load_dotenv
load_dotenv()


def report_about_costs(start_date, end_date, store):
    """
    :param start_date: 2020-09-23 will be + 00:00:00
    :param end_date: 2020-09-23 will be 23:59:59
    :param store: moscow_store, green_house, saratov, internet
    :return: [{'store': moscow, 'quantity': 7, 'sum': 123123.0, 'date': 'start_date, end_date'}
    """
    headers = {
        "Content-Type": "application/json",
        # "Lognex-Pretty-Print-JSON": "true",
        "charset": "UTF-8"
    }
    store_ = os.getenv(store)
    auth = (os.getenv('moysclad_login'), os.getenv('moysclad_pass'))
    request_url = f"https://online.moysklad.ru/api/remap/1.2/report/sales/plotseries?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:59&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{store_}"
    response_moscow = requests.get(request_url, auth=auth, headers=headers)
    stock = response_moscow.json()
    series = stock.get('series')
    info_about_costs = {'store': store,
                        'quantity': 0,
                        'sum': 0,
                        'date': (start_date, end_date)}
    for day in series:
        info_about_costs['quantity'] += day.get('quantity')
        info_about_costs['sum'] += day.get('sum')
    return info_about_costs
