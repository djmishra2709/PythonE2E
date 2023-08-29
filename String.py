a='String1'
b="String2"

print("====================================")

print(a,b)
c= "hi Dheeraj 'My name is Rohan'"
d= 'hi Dheeraj "My name is Rohan"'
print(c , d)

print("====================================")

print(a[0])  #s
print(a[4])  #n

print("====================================")
for char in a:
    print(char)

print("====================================")
#print(a[10])  # throw index out of range

print("================String slicing====================")

name="Dheeraj,mishra"
name1="Harry"
print("Length of string is :",len(name))  #Length of string is : 14
print(name[0:5])                          #Dheer (python neglect last index with positive index)
print(name[1:5])                          #heer
print(name[:3])                           #Dhe
print(name[:])                            #Dheeraj,mishra
print(name[0:-1])                         #Dheeraj,mishr
print(name[-6:-1])                        #mishr (we can convert this line in line 33 which is equivalent to line 32 and give same output)
print(name[len(name)-6:len(name)-1])      #mishr
print(name1[-4:-2])                        #ar

print("================String Methods====================")

name="$$$$Dheeraj,mishra$$$$"
print("length of name is:",len(name))
print(name.upper())
print(name.lower())
print(name.rstrip("$"))
print(name.replace("mishra","jha"))
print(name.split(","))
print(name.capitalize())
print("count of e in string is:",name.count("e"))
print(name.endswith("mishra"))
print(name.startswith("$"))
print(name.endswith("mishra",4,18))
print(name.find(":"))    #it will return -1 if not found , donot throw error
print(name.index(","))   #it will throw error if not found
print(name.islower())
print(name.swapcase())
print(name.isspace())
