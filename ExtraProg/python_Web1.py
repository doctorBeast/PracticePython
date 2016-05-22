'''
This program gives the sum of all the numbers in a file .
'''
import re

fo = open('actual.txt','r')
numblist=[]
for line in fo:
    y=re.findall('([0-9]+)',line)
    if len(y)>0:
        numblist = numblist + y
sum=0
fo.close()
#b=sum(numblist)
numblist = [int(i) for i in numblist]
for i in numblist:
    print(i)
    sum=sum+i

print(sum)