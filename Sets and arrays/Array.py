import array as arr
a1=arr.array('i',[1,3,5,7,9,6,3,9])
print("Original Array :",str(a1))
print("Number of occurences of 3 = ",a1.count(3))
a1.reverse()
print("Reverse the order of the items : ")
print(str(a1))

a1.insert(3,4)
a1.append(5)
print(a1)
