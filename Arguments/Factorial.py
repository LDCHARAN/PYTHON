def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
print(fact(7))
print(fact(10))