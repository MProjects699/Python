numbersTaken = [2, 8, 10, 18]

print("Here are still available some number")

for n in range(1,20):
    if n is numbersTaken:
        continue
        print(n)
