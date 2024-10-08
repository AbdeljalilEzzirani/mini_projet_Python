from functools import reduce

fruits_prices = {"apple": 10, "banana": 45, "avocado": 20, "pineapple": 30}

def add_prices(total, fruit):
    if fruit.startswith('a'):
        return total + fruits_prices[fruit]
    return total

total_price = reduce(add_prices, fruits_prices.keys(), 0)

print("Total price of fruits starting with 'a':", total_price)
