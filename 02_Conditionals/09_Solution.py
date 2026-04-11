# Find a Leap Year
year = int(input("Enter your Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"is a Leap Year!")
else:
    print(year,"Is Not a Leap Year.")