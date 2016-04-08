fo = open('Account.txt','r')
lis=[]
i=0
while True:
    str=fo.readline()
    if str == '':
        fo.close()
        break
    else:
        lis.append(str)
        i+=1

k=0
for i in range(len(lis)):   #not working if typing the statement 'for i< len(lis):'
    if k<=len(lis[i]):
        k=len(lis[i])
        
i=0

for i in range(len(lis)):
    str=list(lis[i])
    if (i!=len(lis)-1):
       del str[-1]

    for j in range(k-len(str)):

        str = [' ']+str
    lis[i]=''.join(str)

fo=open('Account.txt','w')
fo.seek(0)
fo.truncate()

for i in range(len(lis)):
    fo.write(lis[i])
    fo.write('\n')

fo.close()



