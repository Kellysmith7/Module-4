"""Program to calculate order total
Author: Kelly Smith
Program: calculate_order.py
Last updated: 09/17/2019
"""


def calculate_order(price, cash_coupon, percent_coupon):
    SHIP_UNDER_TEN = 5.95
    SHIP_TEN_THIRTY = 7.95
    SHIP_THIRTY_FIFTY = 11.95
    SHIP_OVER_FIFTY = 0
    price_after_cash_coupon = price - cash_coupon
    price = price_after_cash_coupon
    price_after_percent_discount = price - (price * percent_coupon)
    price = price_after_percent_discount
    if price < 10:
        price = price + SHIP_UNDER_TEN
    elif 10 < price < 30:
        price = price + SHIP_TEN_THIRTY
    elif 30 < price < 50:
        price = price + SHIP_THIRTY_FIFTY
    else:
        price = price + SHIP_OVER_FIFTY
    return price


if __name__ == '__main__':
    print("Final price is:  $%5.2f" % calculate_order(25, 10, .15))
