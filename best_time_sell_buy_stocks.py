
# Dynamic Programming: Find maximum single sell profit Given a list of daily stock prices(integers for
# simplicity), return the buy and sell prices for making the maximum profit. We need to maximize the
# single buy / sell profit.If we can’t make any profit, we’ll try to minimize the loss.
# [8, 5, 12, 9, 19, 17]
# [8, 5, 12, 9, 19, 1]
# [21, 12, 11, 9, 6, 3]

stock_prices = [8, 5, 12, 9, 19, 1]


def stock_sell_purchase(stock_prices_list):
    new_list = []
    len_list = len(stock_prices_list) - 1
    b_price = min(stock_prices_list)
    if b_price is not stock_prices_list[len_list]:
        s_price = find_max_value(stock_prices_list, b_price)
    else:
        s_price = func_calculates_difference(stock_prices_list)
        for i in range(len_list-1):
            new_list.append(stock_prices_list[i])
        b_price = min(new_list)

    return b_price, s_price


def find_max_value(stock_list, price):
    new_list = []
    index = stock_list.index(price)
    start = (index + 1)
    end = (len(stock_list) - 1)

    for item in range(start, end):
        new_list.append(stock_list[item])
    max_p = max(new_list)

    return max_p


def func_calculates_difference(list_d):
    new_list = []
    for i in range(len(list_d) - 1):
        new_list.append(list_d[i])
    if max(new_list) == list_d[0]:
        least_diff = min(new_list)
    else:
        least_diff = max(new_list)
    return least_diff


buy_price, sell_price = stock_sell_purchase(stock_prices)
print(buy_price, sell_price)
