def decode(str1):
    s=""
    length=len(str1)
    for i in range(length):
        if ord(str1[i])>= 65 and ord(str1[i])<90 :
            ch= chr(ord(str1[i])+1)
            s=s+ch
        if ord(str1[i])==90:
            s=s+chr(65)
        if ord(str1[i])==122:
            s=s+chr(97)
        if ord(str1[i])==32:
            s=s+" "
        if ord(str1[i])==44:
            s=s+","
        if ord(str1[i])==46:
            s=s+"."
    return s


str=input("Enter the messege: ")
str=str.upper()
new_str=decode(str)
print("The Decoded String is: ", new_str)