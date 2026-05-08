# ✏️ Write a function called grade that takes a score (0-100) and returns the letter grade.
# grade(95)  → "A"
# grade(85)  → "B"
# grade(75)  → "C"
# grade(65)  → "D"
# grade(50)  → "F"

# Per = int(input("Enter Your Percentage: "))


def grade(per):
    if per < 0 or per > 100:
        return "Invalid! Enter a number between 0 and 100"
    elif per >= 90:
        return "A"
    elif per >= 80:
        return "B"
    elif per >= 70:
        return "C"
    elif per >= 60:
        return "D"
    else:
        return "F"


print(grade(80))  # B
print(grade(95))  # A
print(grade(-5))  # Invalid!
print(grade(101))  # Invalid!
