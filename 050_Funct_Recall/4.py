# ✏️ Write a function called calculate that takes two numbers and an operation (as a string), and returns the result.
# calculate(10, 5, "add")       → 15
# calculate(10, 5, "subtract")  → 5
# calculate(10, 5, "multiply")  → 50
# calculate(10, 5, "divide")    → 2.0

# def calculate (num1,num2):
#     return num1 + num2, num1 - num2, num1 * num2,num1 / num2
# print(calculate(10,5))

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        return num1 / num2
    else:
        print("Invalid!")
print(calculate(10,5,"add"))
print(calculate(15,5,"multiply"))
print(calculate(40,15,"subtract"))
print(calculate(10,20,"divide"))