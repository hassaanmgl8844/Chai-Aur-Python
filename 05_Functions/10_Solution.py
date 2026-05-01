# Create a Recursive Function to calculate the factorial of a Number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)