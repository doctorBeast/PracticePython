#also think about what should be the output if the input strings are actAml, actTml, actaml
#has some issues if the input characters are capitalized
def srtchar():
    list = []
    corresponding_list=[]
    while True:
        ch = input('Type the string and to sort type \'exit\'')
        if ch.lower() != ch:
            corresponding_list.append(1)
        else:
            corresponding_list.append(0)
        if ch != 'exit':

            list.append(ch)
        else:
            list.sort()
            break
    '''
    #if flag =1 then the first letter of that word is to be capitalized
    for x in range(len(list)):
        if corresponding_list[x] is 1:
            list[x].[:1]
    '''
    print(list)

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


