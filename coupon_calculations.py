def calculate_price(price):
    if price < 10:
        return price + 5.95
    elif 10 < price < 30:
        return price + 7.95
    elif 30 < price < 50:
        return price + 11.95
    else:
        return price


def calculate_order(price, cash_coupon, percent_coupon):
    dollar_result = price - cash_coupon
    percent_result = dollar_result * percent_coupon / 100
    order_total = dollar_result - percent_result
    return order_total
