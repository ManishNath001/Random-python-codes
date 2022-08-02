dict1={}
key=0
value=0
num=int(input("Enter the number of elements:"))
for key in range(num):
    value=int(input("Enter the value:"))
    dict1[key]=value
lis=[]
lis=sorted(dict1.values(), reverse=True)
print("Three highest values:")
for i in range(3):
    print(lis[i])