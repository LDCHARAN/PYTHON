d1={'a':10,'b':20,'c':30,'d':40,'e':50,'f':60}
print(d1)
d1={'a':10,'b':20,'c':30,'d':40,'e':50,'f':60,'c':70}
print(d1)
#access any value from dictionary
print(d1['d'])
#Modify a value for any key
d1['b']=200
print(d1)
#delete the value
x=d1.pop('d')
print("value of the deleted key",x)#value of deleted key
print(d1)
x=d1.popitem()
print("value of the deleted key",x)#value of deleted key
print(d1)
x=d1.get('f')
print("The value at the key 'f'",x)

#access keys
c=0
for k in d1:
    c=c+1
    print("Key ",c,":",k)
#access keys
c=0
for k in d1.keys():
    c=c+1
    print("value ",c,":",k)
#access values
c=0
for v in d1.values():
    c=c+1
    print("value ",c,":",v)
#access keys and values
c=0
for k,v in d1.items():
    c=c+1
    print(c,") key : ",k,"value:",v)