# age  = int(input("What is Your Age: "))
# if age > 18:
#     print("You're Adult")
# else:
#     print("You're a Minor")

# Ask user to enter a number
# If number is positive → print "Positive"
# If number is negative → print "Negative"
# If number is zero → print "Zero"
user = int(input("Enter a Number: "))
if user % 2 == 0:
    print("This is Postive Number.")
elif user % 3 == 0:
    print("This is Negative Number.")
else:
    print("You're Printing Zero Baby!")