n=int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i),"*"*i)
    


        
j = 1
for i in range(n, 0, -1):
    print(" " * i, "*" * (2*j-1))
    j += 1



for i in range(1, 10):
    if i < 6:
        print("*"*(6-i)+ " "*((i*2)-2)+"*"*(6-i))
    else:
        print("*"*(i-4)+ " "*(((10-i)*2)-2)+"*"*(i-4))


for i in range(0, n+1):
    num = 0
    for j in range(n, 0,-1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num+1, end=' ')
            num += 1
    print("")       

for i in range(1,n+1):
    for j in range(1, n+1-i):
        print(' ', end='')
    for j in range(1,i+1):
        print(j, end='')
    for j in range(i-1,0,-1):
        print(j, end='')
    print()

for i in range(1,n+1):
    for j in range(1, n+1-i):
        print(' ', end='')
    for j in range(i,0,-1):
        print(j, end='') 
    for j in range(2,i+1):
        print(j, end='')
    print()

