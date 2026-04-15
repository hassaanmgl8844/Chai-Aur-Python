number = int(input("Enter a Number: "))

for i in range (1,11):
    if i == 5:
        continue
    print(number , "x" , i , "x" , number * i)