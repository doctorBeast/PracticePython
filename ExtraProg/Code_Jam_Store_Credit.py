import itertools

def find(tem_lis , Cash):
    m = 0
    n = 0
    for pair in itertools.combinations(tem_lis , 2):
        if pair[0] + pair[1] == Cash:
            m,n = pair[0],pair[1]
            break
        else:
            continue
    return (m,n)


N = int(input("Enter the number of cases :"))
final = {}
for i in range(N):
    lis = []
    C = int(input("How much amount do you have :"))
    I = int(input("How many items do you have :"))
    price = input("Price of items :")
    lis = price.split()
    for j in range(len(lis)):
        lis[j] = int(lis[j])

    a,b = find(lis, C)
    a=lis.index(a)+1
    b=lis.index(b)+1

    final['Case %s' %(i+1)]=[a,b]

for i in range(N):
    print('Case %s :'%(i+1),final['Case %s'%(i+1)])