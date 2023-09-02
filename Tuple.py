# tuple can not be manipulated, it will be fixed(unchangeable)
print("==================================")
tuple1 = (1,2,3,4,5,5,6,7)
print(tuple1)
print(tuple1[-1])


print("==================================")
tuple2=tuple1[1:5]
print(tuple2)
print(tuple2[1:])
print(tuple2[:1])

print("========operation on tuple==========")

print(tuple1.index(3)) # first occurance of 3
print(tuple1.index(7,5,8)) # first occurance of 7 between 5 and 8 index
print(len(tuple2))

print("=================convert tuple into list=================")

list2 =list(tuple1)
print(list2)
list1=[i+2 for i in list2]
print(list1)
tuple1=tuple(list1)
print(tuple1)

