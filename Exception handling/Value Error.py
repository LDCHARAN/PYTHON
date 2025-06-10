try:
    n=int(input("Except a number : "))
    print("the number entered is : ",n)
except ValueError as ex:
    print("Exception:",ex)