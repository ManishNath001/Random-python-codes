lis1=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    str=input("Enter the element:")
    lis1.append(str)
ran=int(input("Enter the max length of words:"))
lis2=[]
for x in lis1:
    if len(x)>ran:
        lis2.append(x)
print("List of words larger than the given range:",lis2)