# ✏️ Write a function called sum_list that takes a list of numbers and returns their sum — without using Python's built-in sum()!
# sum_list([1, 2, 3, 4, 5])  → 15
# sum_list([10, 20, 30])     → 60

# sumli = [1,2,3,4]
# def sum_list(sumli):
#     for i in sumli:
#         count = count + 1
#     return sumli()

# print(sum_list())


def sum_list(numbers):
    total = 0
    for i in numbers:
        total = total + i  
    return total  


print(sum_list([1, 2, 3, 4, 5]))
