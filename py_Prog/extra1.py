'''
This is a new type of sorting
In this I will take the average of the whole data
start the loop from index 0
if the number is less than avg then increment the index value
if the number is greater then swap it with the last element and decrement the counter that will point at the last element.
keep notice of the counter that starts from the back.
'''


def sort(inlist):
    sum=0
    l=len(inlist)
    i=0
#    flag=2
    for num in inlist:
        sum+=num

    try:
        avg=sum/len(inlist)
        print(avg)
    except ZeroDivisionError:
        pass
    while i<l :
        if inlist[i]<avg:
            i+=1
#            flag=0
        elif inlist[i]==avg:
            i+=1
            pass
        else:
            l-=1
            m=inlist[i]
            inlist[i]=inlist[l]
            inlist[l]=m
#            flag=1
    if l== len(inlist):
        return inlist
    if len(inlist)>1:
        inlist[0:l] = sort(inlist[0:l])
        inlist[l:len(inlist)] = sort(inlist[l:len(inlist)])

    return inlist




lis=[3,7,2,1,5,9,3]

lis=sort(lis)
print(lis)