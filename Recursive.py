print("================================")
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)

c =factorial(3)
print(c)

print("================================")

def fabonnacci(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return