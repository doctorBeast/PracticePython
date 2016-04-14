#find value of pi upto 30 decimal places

a=1
b=['3.']
for x in range(30):
    a = a*10
    c=str(int(a/7))
    b=b + [c]
    a = a%7

m=''

for x in range(len(b)):
   m=m+b[x]

print(m)