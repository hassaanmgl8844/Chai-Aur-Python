n = int(input("Enter a Number: "))
sum_even = 0

for i in range(1,n+1):
    if i%2 == 0:
        sum_even += 1
print("Even Sum of N is: ",sum_even)