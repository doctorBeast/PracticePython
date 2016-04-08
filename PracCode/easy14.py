lis=[]

while True:
    txt = input('Type what to add:')
    if txt=='':
        break
    else:
        lis.append(txt)

i=0
print(len(lis))
while i < (len(lis)-1):
    m=lis[i]
    lis[i]=lis[i+1]
    lis[i+1]=m
    i+=2

print(lis)