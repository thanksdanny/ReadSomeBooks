prices = {
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM' : 37.20,
    'FB' : 10.75
}
print(zip(prices.values(), prices.keys()))
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)