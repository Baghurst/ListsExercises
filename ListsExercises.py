A = [1,2,'a','c',4.4,'CCbio','l','k','9',0,0]
print(A)

L = []
L = ['value', ...]
print(L)
sqrs = [0,4,2343,34343,34344,5466,655656,565656,7777777,777777777777,777777777,
77,8987,54543,233,23423,2324,346,57,686868,6,78]
print(sqrs)

L1 = [3, 4, [5, 6], 7]
print(L1)

LL = list("aaa")
print(LL)

L1= list(input("Enter list elements: ")) 
print(L1)
list = eval(input("Enter list to be added: " ))
print ("list you entered :", list)

J = eval('5+8')
print(J)

y= eval("3*10")
print(y)

y= eval("2+2")
print(y)

var1 = eval(input("Enter Value:"))
print(var1,type(var1))

L = ['P','y','t','h','o','n']
for a in L :
    print(a)

L=['q','w','e','r','t','y']
lenght = len(L)
for a in range(lenght) :
    print("At indexes", a, "and", (a - lenght), "element :", L[a])

X=L+L1
print(X)

lst =[10,12,14,20,22,24,30,32,34]
seq = lst [3:-3]
print(lst)

L1, L2 = [1, 2, 3], [1, 2, 3]
L3 = [1, [2, 3]]
'''L1 == L2 # Statement seems to have no effect'''
'''print(L1, L2, L3) # Statement seems to have no effect'''
'''L1 == L3 # Statement seems to have no effect'''
'''print(L1,L2,L3) # Statement seems to have no effect'''

lst1 = [1,3,5]
lst2 = [6,7,8]
lst3 = lst1 + lst2
print(lst3)

"""lst = [10,12,20,22,24,30,32,34] #Not working how it's supposed to.
lst2 = lst [3:25]
print(lst)
lst3 = lst[::3]
print(lst3)"""

lst = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ]
slc1 = lst[5 : 13 :2]
slc2 = lst[::4]
sum = avg = 0
print("Slice 1")

for a in slc1 :
    sum += a
    print (a, end = ' ')
print ()
print ("Sum of elements of slice 1:", sum)
print ("Slice 2")
sum = 0
for a in slc2 :
    sum += a
    print (a, end = ' ')
print()
'''avg = sum / len(slc2) #Incompatible types in assignment
(expression has type "float", variable has type "int")  [assignment]''' 

print ("Average of elements of slice 2:", avg)

'''del lst[10] #Not sure if it worked how it's supposed to.
lst
print(lst)'''

'''lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, #Not working how it's supposed to.
16,17,18,19,20]
lst.pop()
print(lst)
lst.pop(10)
print(lst)'''
item1 = [1,2,3,4,5,6,7,8,9]
item2 = [12,13,14,15,16,17]
item3 = [21,23,25,26,27,28]
'''item1 = L.pop()              #last item #  # Incompatible types
in assignment (expression has type "str", variable has type "list[int]")  [assignment]
item2 = L.pop(0)             #first item
item3 = L.pop(5)             #sixth item'''

a = [1,2,3]
b = a

a = [1,2,3]
b = a
a[1] = 5
print(a,b)

colours = [ 'red', 'green', 'blue']
colours.append("yellow")
print(colours)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
print(t2)

t1.insert(-9, 'k')
print(t1)

#Didn't really understand the pop() method.
t1 = ["k", "a", "e", "i", "p", "q", "u"]
ele1 = t1.pop(0)
print(ele1)
'''t1,remove("k")
print(t1)# Not working for some reason'''
t1.reverse()
print(t1)

t1 = ['b','d','c','a','f','h','e','g']
t1.sort()
print(t1)

