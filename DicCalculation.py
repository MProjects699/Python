stocks = {
    'GOOG':434,
    'GOOG': 434,
    'GOOG': 434,
    'GOOG': 434,
}

#(434, GOOG) (325, AAPL)
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)