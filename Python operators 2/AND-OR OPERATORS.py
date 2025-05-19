#and-or operators
a,b,c,d=3,8,0,0
if a and b:
    print(a,'and',b,'are true values')
elif a or b:
    print('Either',a,'or',b,'is a true value')
else:
    print(a,'and',b,'are false')

if b and c:
    print(c,'and',b,'are true values')
elif c or b:
    print('Either',c,'or',b,'is a true value')
else:
    print(c,'and',b,'are false')

if d and c:
    print(d,'and',c,'are true values')
elif c or d:
    print('Either',c,'or',d,'is a true value')
else:
    print(c,'and',d,'are false')

print("value of b=",b,"and value not b =",not b)
print("value of c=",c,"and value not b =",not c)