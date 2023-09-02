print("===========================")
#do not contain duplicate values
#doen not follow order

set1 ={2,4,6,9,2}
print(set1)

set2 ={2,"dheeraj",4,5}
print(set2)

#empty set
set3=set()

#empty dictionary
dict={}

for n in set1:
    print(n)

print("============================")

set4= {1,4,3,2,7,8}
set5={3,4,7,8}

print(set4.union(set5))
#set4.update(set5)  # it add num in set4 which are not common in set5
print(set4.intersection(set5))
print(set4.symmetric_difference(set5))

print("============disjoint================")

print(set4.isdisjoint(set5))

print(set4.issubset(set5))

print(set4.issuperset(set5))

print("============delete================")
set6={3,4,7,8}
del set6
#print(set6)

print("============iterating sets================")

for n in set4:
    print(n)

if 7 in set5:
    print("present")
else:
    print("absent")

