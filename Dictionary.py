print("===================simple===========================")
dict1={
    "name":"Dheeraj",
    "Age":30,
    "Address":"pune",
    "married":True
}

print(dict1["name"])             # this will throw key error if not present
print(dict1.get("married1"))     # this will return none if not present
print(dict1)


print(dict1.keys())
print("===================keys()===========================")

for n in dict1.keys():
    print(dict1.get(n))
    print(f"key is {n} and its value is {dict1[n]}")
print("===================value()===========================")

for m in dict1.values():
    print(m)

print("==================items()============================")

for key,value in dict1.items():
    print(f"key is {key} and its value is {value}")

print("==================methods============================")

dict2={
    "salary" :1000,
    "company":"wipro"
}
dict1.update(dict2)  # add all items of dict2 into dict1
print("updated dictionay:",dict1)

dict1.popitem()   #last key pair will be deleted
print(dict1)

print(dict2)
del dict2["company"]
print(dict2)