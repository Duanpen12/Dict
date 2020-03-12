price_and_stock = {}

prices = {
    "banana": 3,
    "apple": 2,
    "orange": 1.5,
    "pear": 4
    }

stock_availability = {
    "banana": 10,
    "apple": 10,
    "orange": 10,
    "pear": 10
    }

for fruit in prices.keys():
    price = prices.get(fruit)
    stock = stock_availability.get(fruit)
    print("fruit: %s, price: %d, stock: %d" % (fruit, price, stock)) # just for debug
    price_and_stock[fruit] = {'price': price, 'stock': stock}

# can be printed like this:
print(price_and_stock)

# or with iterating like this:
for fruit, parameters in price_and_stock.items():
    print("%s: %s" % (fruit, parameters))
