m=int(input("\nEnter the number of rows or column: "))
n=m
a=[]
f=0
print("\nEnter the elements separated by ',' : ")
t=input().split(',')
t=[int(item) for item in t]
a=[]
while t!=[]:
    a.append(t[:n])
    t=t[n:]
print("\nThe original matrix is: ")
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
for i in range(n):
    row_min=a[i][0]
    ci=0
    for j in range(1,n):
        if row_min>a[i][j]:
            row_min=a[i][j]
            ci=j
    k=0
    while k<n:
        if row_min<a[k][ci]:
            break
        k+=1
    if k==n:
        print("\nThe saddle point is: ",row_min)
        f=1
if(row_min % 2==0):
    print("The Saddle point is even.")
else:
    print("The Saddle point is odd")

if row_min > 1:  
    for l in range(2, int(row_min/2) + 1):  
        if (row_min % l) == 0:  
            print("The Saddle point is not prime")  
            break  
    else:  
        print("The Saddle point is prime")  
else:  
    print("The Saddle point is not prime") 
if f==0:
    print("\nSaddle point does not exist")