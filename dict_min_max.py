dict1={}
key=0
value=0
num=int(input("Enter the number of elements:"))
for key in range(num):
    value=int(input("Enter the value:"))
    dict1[key]=value
print("maximum value=", max(dict1.values()))
print("minimum value=", min(dict1.values()))