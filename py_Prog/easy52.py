import operator

lis = ['Hello','this','is','me','how','you','doing']

dif = {}
for i in range(len(lis)):
    lis[i]=lis[i].lower()
    temp_lis = list(lis[i])
    sum = 0
    for j in range(len(temp_lis)):
        sum +=(ord(temp_lis[j])-96)
    dif[lis[i]]=sum

final = sorted(dif.items(), key = operator.itemgetter(1) )

lis[:] = []
for i in range(len(final)):
    lis.append(final[i][0])

print(lis)