# ✏️ Write a function called max_of_two that takes two numbers and returns the bigger one
# max_of_two(3, 7)  → 7
# max_of_two(10, 4) → 10

def max_of_two (num1,num2):
    if num2 > num1:
        return num2
    elif num1 > num2:
        return num1
    else:
        return num1
print(max_of_two(11,11))