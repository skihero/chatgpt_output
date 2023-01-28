
def average_down(stock_price, shares_bought, new_price):
    total_cost = shares_bought * stock_price
    new_shares = shares_bought + (total_cost / new_price)
    new_average = total_cost / new_shares
    return new_average

#Example usage
current_price = 100
shares_owned = 10
new_price = 90
average_down_price = average_down(current_price, shares_owned, new_price)
print("The new average price after averaging down is:", average_down_price)

