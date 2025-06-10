#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mult(a,b):
    c=a*b
    return c

def div(a,b):
    c=a/b
    return c

print("Please the select the operation to be performed ")
print("1.Add")
print("2.Subtraction")
print("3.Multiplication")
print("4.division")
ch=int(input("Enter your choice"))
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
if ch==1:
    print(n1,"+",n2,"=",add(n1,n2))
elif ch==2:
    print(n1,"-",n2,"=",add(n1,n2))
elif ch==3:
    print(n1,"*",n2,"=",add(n1,n2))
elif ch==4:
    print(n1,"/",n2,"=",add(n1,n2))
else:
    print("Invalid option")