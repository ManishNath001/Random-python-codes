dict1={}
key=0
num=int(input("Enter the number of elements:"))
for key in range(num):
    value=int(input("Enter the value:"))
    dict1[key]=value

print("Sum of all elements=",sum(dict1.values()))