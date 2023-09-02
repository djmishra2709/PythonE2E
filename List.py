print("=====================================")
marks =[20,30,40,10,90,100,50,30]
print(marks)
print(marks[0])

print("=====================================")

details =["Dheeraj",30]  # contains different data types
print(details)
print(details[-1])       # you can convert into details[len(detals)-1]]

print("=====================================")

if 30 in details: # we can use in keywork to check any value in a list
    print("yes")
else:
    print("No")

print("==============jump index=======================")
print(marks)
print(marks[1:-1])
print(marks[1:-1:2]) # last argument is jump index , i will jump 2 index with current index

print("==============list comprehension=======================")

list =[i*5 for i in range(10)]
print(list[1:])
list1 =[i*5 for i in range(10) if i%6==0]
print(list1)

print("================list manipulation=====================")
marks.append(88)
marks.sort()
marks.sort(reverse=True)
print(marks)
print(marks.count(88))

n = marks.copy()   #create a copy of marks and marks can not be modified
n[0]=199
n.reverse()
print(n)
k=n+marks       # merge two lists
print(k)



