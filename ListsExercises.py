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
L0 = L1 == L2
print(L0) 
a=L1 == L3 
print("A:",a,L1,L2,L3)

lst1 = [1,3,5]
lst2 = [6,7,8]
lst3 = lst1 + lst2
print(lst3)

lst = [10,12,20,22,24,30,32,34]
lst2 = lst [3:25]
print(lst,lst2)
lst3 = lst[::3]
print(lst3)

lst = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ]
slc1 = lst[5 : 13 :2]
slc2 = lst[::4]
sum_ = avg = 0
print("Slice 1")

for a in slc1 :
    sum_ += a
    print (a, end = ' ')
print ()
print ("Sum of elements of slice 1:", sum)
print ("Slice 2")
sum_ = 0
for a in slc2 :
    sum_ += a
    print (a, end = ' ')
print()
avg = sum_ / len(slc2)

print ("Average of elements of slice 2:", avg)
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
del lst[10] #Not sure if it worked how it's supposed to.
print("HEllo",lst)
q=lst.pop(4)
print("Hello2",lst,"Q:",q)
lst.pop(10)
print("Hello3",lst)
item1 = [1,2,3,4,5,6,7,8,9]
item2 = [12,13,14,15,16,17]
item3 = [21,23,25,26,27,28]
L = [41,23,65,26,97,28]
item1 = L.pop()   
item2 = L.pop(0)             #first item
item3 = L.pop(3)             #sixth item'''

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


t1 = ["k", "a", "e", "i", "p", "q", "u"]
ele1 = t1.pop(0)
print(ele1)
t1.remove("a")
print(t1)
t1.reverse()
print(t1)

t1 = ['b','d','c','a','f','h','e','g']
t1.sort()
print(t1)

lst = eval(input("ENTER list : "))
length =len(lst)
min_ele = lst[0]
min_index = 0
for i in range(1, length) :
    if lst[i] < min_ele :
        min_ele = lst[i]
        min_index = i
print("Given list is : ", lst)
print("The minimum element of the given list is :")
print(min_ele, "at index", min_index)
lst = eval(input("ENTER LIST : "))
length = len(lst)
mean = sum = 0
for i in range(0, length) :
    sum += lst[i]
mean = sum /length
print("Given list is :", lst)
print("The mean of the given list is :", mean)
lst = eval(input("Enter list :"))
length = len(lst)
element = int(input("Enter element to be searched for :"))
for i in range(0, length) :
    if element == lst[i] :
        print(element, "found at index", i)
        break
else :               # else of for loop
    print(element, "not found in given list")
    
#11.6 Not working!
print("***11.6***")    
lst = eval(input("Enter list: "))
lenght= len(lst)
element = int(input("Enter element: "))
count=0
for i in range(0,lenght):
    if element -- list[i]:
        count += 1
if count == 0 :
    print(element, "not found in given list")
else :
    print(element, "has frequency as", count, "in given list")

