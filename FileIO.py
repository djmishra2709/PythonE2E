# read mode will be default
f= open('file.txt','r')
print(f.read())
f.close()

# writing a file
f= open('file.txt','w')
f.write("Hello world")
f.close()

# writing a file
f= open('file.txt','a')
f.write("\n|||Hello world|||")
f.close()

#using with keyword

with open('file.txt','a') as f:
    f.write("\nThis is with example")

print("=============readline=====================")

f= open('file.txt','r')
while True:
    line=f.readline()
    if not line:
        break

    print(line)

print("=============writeline=====================")

f= open('file.txt','w')
lines="my name is Dheeraj....."
f.writelines(lines)
f.close()

