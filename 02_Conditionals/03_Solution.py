# Grade Calculator
Per = int(input("Enter Your Percentage: "))

if Per >= 101:
    print("Please Enter Your Percentage Again!")
    exit()

if Per >= 90:
    print("You Got A Grade!")
elif Per >= 80:
    print("You Got B Grade!")
elif Per >= 70:
    print("You Got C Grade!")
elif Per >= 60:
    print("You Got D Grade!")
else:
    print("You Got F Grade. You Need To Work Hard!")
