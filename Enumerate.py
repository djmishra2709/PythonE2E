
#Enumerates return tuple with index and value at same time

print("=========without enumerate==============")
marks=[12,34,65,2,90,80,60]
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("Good one")
    index=index+1

print("=========with enumerate=================")

for index, mark in enumerate(marks):
    print(mark)
    if(index==5):
        print("Awesome.....")

print("=========with enumerate custom start point=================")

for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index==5):
        print("Awesome.....")