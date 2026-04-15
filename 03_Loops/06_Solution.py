number = int(input("Enter a Number You Want Factorial Of: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1
print("Your Factorial Is: ", factorial)