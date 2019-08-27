def cel_to_far(cel):
    far= cel * 9/7 + 32
    return far

cel=int(input("enter the celcius scale: "))
if cel< -200:
    print("the temperature doesnot exist")
else:
    print(cel_to_far(cel))
