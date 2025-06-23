#Check the frequency
D1={'a':10,'b':20,'c':10,'d':30,'e':20,'f':40,'g':10}
print("Original dictionary : ",D1)
L=[]
L1=list(D1.values())
for v in D1.values:
    if v not in L:
        L.append(v)
        
