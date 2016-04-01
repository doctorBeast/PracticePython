#also think about what should be the output if the input strings are actAml, actTml, actaml
import sys

def srtchar():
    lis = []
    corresponding_list=[]
    while True:
        ch = input('Type the string and to sort type \'exit\'')
        if ch.lower() != ch:
            corresponding_list.append(1)
        else:
            corresponding_list.append(0)

        if ch != 'exit':

            lis.append(ch)
        else:
            lis.sort()
            breakL
            #found the fault....i have rearrange the corresponding list as the list
    '''
    #if flag =1 then the first letter of that word is to be capitalized
    for x in range(len(lis)):
        m=x-1
        if corresponding_list[m] is 1:

            #list[x][:1] = chr(ord(list[x][:1])+26)

            a=list(lis[m])
            a[0]=chr(ord(a[0])+32)
            str="".join(a)
            if m == 0:
                print(str)
            lis[m]=str
    '''
    print(lis)
    print(corresponding_list)

def srtnum():
    list=[]
    while True:
        num = input('Type the string and to sort type any character')
        if num.isdigit():
            num = int(num)
            list.append(num)
        else:
            list.sort()
            break

    print(list)


a = input("What do you want to sort , characters or numbers ")
print(a.lower())
if a.lower()=='characters':
    srtchar()
elif a.lower()=='numbers':
    srtnum()
else:
    print('invalid entry')


