# Password Strength Checker
password = input("Enter Your Password: ")
passwordLength = len(password)

if passwordLength < 6:
    strength = "Weak!"
elif passwordLength <= 10:
    strength = "Medium!"
else:
    strength = "Strong!"

print("Your Strength is: ",strength)