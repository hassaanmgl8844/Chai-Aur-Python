# ✏️ Write a function called is_even that takes a number and returns True if it's even, False if it's odd.
# is_even(4)  → True
# is_even(7)  → False

def is_even(num): 
    if num % 2 == 0: 
        return True
    else:
        return False
is_even(5)              