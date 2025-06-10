try:
    n1,n2=eval(input("Enter two numbers seperated by a comma"))
    res=n1/n2
    print("Result is : ",res)
except SyntaxError:
    print("Comma is missing")
except ZeroDivisionError:
    print("Division by zero is not possible")
except:
    print("Wrong input")
else:
    print("No exeptions")
finally:
    print("Hureyy....this will excecute independent of exception")