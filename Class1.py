list1=["Chandni","Vaibhav","Avipsa","Sandhya","Moksh","Soni"]
list2=[10,"Chandni",11,"Moksh",12,"Avipsa"]
print("List elements are:")
i=0
while i<list2.__len__():
  print("At",i," is",list1[i])
  i=i+1

#list operations
#slice
print(list1[0:2])
print(list1[-4:-1])

#append
list1.append(66)
print("after append:",list1)

#insert
list1.insert(2,"Annu")
print("after insert:",list1)

#extend
list1.extend(list2)
print("after extend:",list1)

#update
list2[1]=1645
print("updated list:",list2)

#delete
del list1[2]
list1.remove("Chandni")
print("after delete:",list1,"after remove:",list1)
List elements are:
At 0  is Chandni
At 1  is Vaibhav
At 2  is Avipsa
At 3  is Sandhya
At 4  is Moksh
At 5  is Soni
['Chandni', 'Vaibhav']
['Avipsa', 'Sandhya', 'Moksh']
after append: ['Chandni', 'Vaibhav', 'Avipsa', 'Sandhya', 'Moksh', 'Soni', 66]
after insert: ['Chandni', 'Vaibhav', 'Annu', 'Avipsa', 'Sandhya', 'Moksh', 'Soni', 66]
after extend: ['Chandni', 'Vaibhav', 'Annu', 'Avipsa', 'Sandhya', 'Moksh', 'Soni', 66, 10, 'Chandni', 11, 'Moksh', 12, 'Avipsa']
updated list: [10, 1645, 11, 'Moksh', 12, 'Avipsa']
after delete: ['Vaibhav', 'Avipsa', 'Sandhya', 'Moksh', 'Soni', 66, 10, 'Chandni', 11, 'Moksh', 12, 'Avipsa'] after remove: ['Vaibhav', 'Avipsa', 'Sandhya', 'Moksh', 'Soni', 66, 10, 'Chandni', 11, 'Moksh', 12, 'Avipsa']
[13]
0s
#Set
set1={2,4,6,23,88}
set2={6,88,56,(1,2),"HELLO"}
print(set1)

#set operations
set1.discard(23)
print("after discard:",set1)

set2.remove("HELLO")
print("after remove:,set2")

set1.pop()
print("after pop:",set1)

set3=set1|set2
print("after union:",set5)

set4=set1^set2
print("after symmetric difference:",set8)
{2, 4, 6, 23, 88}
after discard: {2, 4, 6, 88}
after remove:,set2
after pop: {4, 6, 88}
after union: {1, 2, 3, 4, 5, 6, 7}
after symmetric difference: {1, 2, 6, 7}
tuple=(2,4,6,"f","gg")
print(type(tuple))
print(len(tuple))
#tuple is immutable
<class 'tuple'>
5
