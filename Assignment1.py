import csv
import re

name = input("Enter the file name:")
handle = open(name)
d = handle.read()
y = re.findall('[0-9]+', d)
sum = 0
for i in range(len(y)):
    c = int(y[i])
    sum += c

print(sum)