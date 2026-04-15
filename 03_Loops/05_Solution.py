input_str = input("Enter Anything in TxT: ")

for char in input_str:
    if input_str.count(char) == 1:
        print("Char Count Is: ",char)
        break