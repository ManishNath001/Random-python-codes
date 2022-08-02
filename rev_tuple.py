lis=[]
tup=()
n=int(input("Enter the number of elements in the tuple:"))
for i in range(n):
    num=int(input("Enter the element:"))
    lis.append(num)
    tup=tuple(lis)
tup2=tup[::-1]
print("reverse tuple=",tup2)