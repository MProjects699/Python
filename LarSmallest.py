import heapq

grades = [32, 43, 654, 132, 66, 532]
print(heapq.nlargest(3, grades))

stocks = [
    {'ticket': 'AAPL', 'price':201},
    {'ticket': 'AAPL', 'price': 201},
    {'ticket': 'AAPL', 'price': 201},
    {'ticket': 'AAPL', 'price': 201},
    {'ticket': 'AAPL', 'price': 201},
]

print(heapq.nsmallest(2, stocks, key=lambda stocks: stocks['price']))