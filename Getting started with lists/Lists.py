L=[]
print(L)
L=list()
print(L)

L=[9,1,20,9,3,5,9,20,2]
print(L[2])
print(L[2:7])

L=[9,1,2,9,3,5,9,20,2]
print(L.count(1))
print(L.count(9))

L.append(30)
print(L)
L.extend([6,1,9])
print(L)
L.insert(2,100)
print(L)

x=L.pop(4)
print(L)
print(x)

L.remove(2)
print(L)

L.clear()
print(L)

L=[9,1,2,9,3,5,9,20,2]
L.reverse()
print(L)

L.sort()
print(L)
L.sort(reverse=True)