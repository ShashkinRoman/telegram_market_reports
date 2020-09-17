from telegram_bot.models import MarketOrders, MarketOrdersProducts


def value_orders_date(start_date, end_date):
    """
    :param start_date: '2020-09-15 00:00'
    :param end_date:  '2020-09-15 23:59'
    :return:
    """
    query_orders = MarketOrders.objects.filter(created_at__range=[start_date + ' 00:00', end_date + ' 23:59'])
    count_orders = len(query_orders)
    value = 0
    for order in query_orders:
        value += value_order(order.orderid)
    return value, count_orders


def value_order(order_id):
    """

    :param order_id: {'order_id': 123123} or 123123
    :return:  {'order_id': 123123, 'value': 12312}
    """
    if type(order_id) is dict:
        id_order = order_id.get('order_id')
    if type(order_id) is int:
        id_order = order_id
    query_orders = MarketOrdersProducts.objects.filter(orderid=id_order)
    value = 0
    for product in query_orders:
        value += product.price
    return value