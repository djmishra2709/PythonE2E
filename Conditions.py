print("=========if else================")
a=int(input("Enter your age :"))
if(a>=18):
    print("vote")
    print("inside if block")
else:
    print("not allowed")
    print("inside else")
print("it is outside the if-else")

print("=========elif ================")
b=int(input("Enter your age :"))
if(b>=18):
    print("vote")
    print("inside if block")
elif(b<18 and b>0):
    print("you are kid")
else:
    print("Enter  valid age")

print("=========nested if ================")
b=int(input("Enter your age :"))
if(b>=18):
    print("inside if")
    if(b>60):
        print("inside nested")
        print("age is more than 60")
    else:
        print("age is between 18 to 60")

print("=========match case ================")

x=int(input("Enter your number :"))
match x:
    case 0:
        print("x is zero")
    case 2:
        print("x is 2")
    case _ if x!=5:
        print("it is not 5")
    case _:
        print("value is:",x)



