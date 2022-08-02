lis1=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    num=int(input("Enter the element:"))
    lis1.append(num)

lis2=list(set(lis1))
print("New list without duplicate values:",lis2)