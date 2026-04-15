while True:
    number = int(input("Enter a Valid Number between 1-10: "))
    if 1 <= number <= 10:
        print("Great!")
        break
    else:
        print("Invalid Number! Print Again.")