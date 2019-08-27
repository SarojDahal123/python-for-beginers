def str_len(str):
    return len(str)

str= (input("enter the string "))
if type(str)== int:
    print("integer donot have length")
elif type(str)== float:
    print("float donot have length")
else:
    print(str_len(str))
