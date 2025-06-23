T=()
print(T)
T=tuple()
print(T)

T=(30)
print(T,type(T))
t=(30,)
print(T,type(T))

T=(30)
print(T,type(T))

T=(6,1,8,1,2,9,10)
L=[6,1,8,1,2,9,10]
L[2]=100
print(L)

T=(6,1,8,1,2,9,10)
print(sum(T))
print(max(T))
print(min(T))

t=(5,7,4)
a,b,c=t
print(b)
T=1,a,2,0,2,c
print(T)

#Create list from Tuple
L=list(T)

L=[]
for x in T:
    L.append(x)