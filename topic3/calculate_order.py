def calculate_order(price, cash_coupon, percent_coupon):
    price_after_cash_coupon = price - cash_coupon
    price = price_after_cash_coupon
    price_after_percent_discount = price - (price * percent_coupon)
    price = price_after_percent_discount
    if price < 10:
        price = price + 5.95
    return price


if __name__ == '__main__':
    print(calculate_order(8, 5, .15))
