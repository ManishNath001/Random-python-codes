def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def rv_Int(nm):
    global rv
    if(nm > 0):
        Reminder = nm %10
        rv = (rv *10) + Reminder
        rv_Int(nm //10)
    return rv

rv=0
nterms = int(input("Enter the number of terms:"))
if nterms <= 0:
   print("Please enter a positive integer:")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       m=recur_fibo(i)
 
   print("Reverse of last term:", rv_Int(m))