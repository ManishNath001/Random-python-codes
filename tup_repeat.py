lis=[]
tup=()
n=int(input("Enter the number of elements in the tuple:"))
for i in range(n):
    num=int(input("Enter the element:"))
    lis.append(num)
    tup=tuple(lis)
lis2=[]
for i in tup:
    if tup.count(i)>1:
        lis2.append(i)
lis2=list(set(lis2))
print("repeated elements are:",lis2)