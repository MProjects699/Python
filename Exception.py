while True:
    try:
        number = int(input("what's your favourite number"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
        