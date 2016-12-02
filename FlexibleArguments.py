def numbers(*args):
    total = 0
    for a in args:
        total +=a
        print(total)

        numbers(5)
        numbers(12,18)
        numbers(12,16,24)