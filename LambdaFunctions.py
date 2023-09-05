print("==========without lambda===============")
def double(n):
    return(2*n)

print(double(5))

print("==========with lambda===============")

double= lambda x:x*2
cube = lambda x:x*x*x
avg = lambda a,b,c:(a+b+c)/3
print(double(5))
print(cube(5))
print(avg(5,3,4))

print("===============function as argument======")

def apply(fn,value):
    return fn(value)

print(apply(cube,2))

print("===============anonymous function======================")
print(apply(lambda x:x**2,4))

