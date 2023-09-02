def calculate(a,b):
    if(a>b):
        print(a,":is greater")
    elif(a==b):
        print("both are equal")
    else:
        print(b,": is greater")


def bye():
    print("Bye Bye")

calculate(9,9)
bye()

print("=================function argument=======================")

def calculate(a=1,b=3):
    if(a>b):
        print(a,":is greater")
    elif(a==b):
        print("both are equal")
    else:
        print(b,": is greater")

calculate(1,)

print("==============function with list=====================================")

def average(*numbers): # this will accept list of int
    sum=0
    for n in numbers:
        sum=sum+n

    return sum/len(numbers)

c=average(2,3,4,1)
print(c)
print("==============function with dictionary=====================================")


def details(**names): # this will accept dictionary
    print(names["age"],names["company"])

names(name="Dheeraj",age="30",company="wipro")
details(names)



