lis=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    num=int(input("Enter the element:"))
    lis.append(num)
max=lis[0]
for a in lis:
    if a>max:
        max=a
print("Largest number=",max)