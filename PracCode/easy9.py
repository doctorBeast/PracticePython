#also think about what should be the output if the input strings are actAml, actTml, actaml
import sys

def srtchar():
    lis =[]
    while True:
        ch = input("Type the string and to sort type exit: ")
        ch=ch.lower()
        if ch!='exit':
            lis.append(ch)
        else:
            lis.sort()
            break
    print(lis)
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


