# Fruit Ripness Checker
# Determine If a fruit is Ripe, Overripe or Unripe Based on it's color. (e.g Banana: Green - Unripe , Yellow - Ripe , Brown - Unripe)

banana = input("Enter the Color of Banana: ").lower()

if banana == "yellow":
    print("Banana is Riped. It's Good! You can Eat it.")
elif banana == "green":
    print("Banana is Unripe. If You don't have any option then you can eat it.")
else:
    print("Banana is Not Eatable. Don't Eat it at any costs!")