name="Dheeraj"
for a in name:
    print(a)
print("===================================")
color=["red","yellow","blue","white"]
for b in color:
    print(b)
    for c in b:
        print(c)

print("============break continue=======================")
color=["red","yellow","blue","white"]
for b in color:
    if(b=="blue"):
        break
    else:
        print("continue")
        continue
print("break the loop")
print("===================================")
for k in range(8):
    print(k)
    print(k+1)
print("===================================")
for j in range(4,8):
    print(j)
print("===================================")

for j in range(4,8,2): # last parameter will be added difference of 2 with each iterated number
    print(j)
print("============while loop=======================")

i=0
while(i<=5):
    print(i)
    i=i+1

d=int(input("Enter your age :"))
while(d>=18):
    d = int(input("Enter your age :"))
    print("Here you go...")
else:
    print("out of while loop")

print("==============do while=====================")
