print("======================================")
try:
    a=input("Enter any number:")
    for i in range(1,11):
        print(i*int(a))
except Exception as e:
    print("please enter valid number")

print("======================================")

try:
        a = input("Enter any number:")
        for i in range(1, 11):
            print(i * int(a))
except ValueError as e:
        print("value error")
except IndexError as e:
        print("index error")
finally:
    print("finally block...")

print("=================custom error=====================")

a=input("Enter a number between 1 to 5 :")
if(int(a)<1 and int(a)>5):
    raise ValueError("value is not between 1 and 5")

