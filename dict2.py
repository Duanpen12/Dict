groceries = {"banana", "orange", "apple"}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def comput_bill(food):
    total = 0
    for item in food:
        total = prices[item] + total
        if stock[item] > 0:
            # total = prices[item] + total
            stock[item] -= 1
    return total


print(comput_bill(groceries))
print("stock : ", stock)
print("prices : ", prices)




