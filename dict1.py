prices_stock = {}

price = {
    "banana": 3,
    "apple": 2,
    "orange": 1.5,
    "pear": 4
    }

stock = {
    "banana": 10,
    "apple": 10,
    "orange": 10,
    "pear": 10
    }

for price_fruit, stock_fruit in price.items():
    if price_fruit in stock.keys():
        prices_stock[price_fruit] = stock_fruit, stock[price_fruit]
        print('fruit: %s, price: %d, stock: %d' % (price_fruit, stock_fruit, stock[price_fruit]))

total = 0
for prices in prices_stock:
    print(price[prices] * stock[prices])
    total = total + price[prices] * stock[prices]

print("Totat fruit is ", total, '$')



