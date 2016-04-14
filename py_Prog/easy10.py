#end the input phone number with a digit

lis=['-','(',')','.',' ','0','1','2','3','4','5','6','7','8','9']
tem=['-','(',')','.']

str = input('type the phone no. : ')

str=list(str)
k=0
flag = 0

for x in range(len(str)):
    ch = str[x]
    if ch not in lis:
        print('Invalid number1')
        k=0
        break
    if ch.isdigit() is True:
        k+=1


if k is 10:
    if str[0] is '(':   #donot start the number with a space
        for x in range(1,4): #because country code is denoted with three characters

            if str[x].isdigit() is False or str[4] is not ')' or str[5] in tem:
                print('Invalid Number1')
                flag=1
                break


        if flag is 0:

            for x in range(5,len(str)):
                if str[x] is ')' or str[x] is '(':
                    print('Invalid Number2')
                    break
                elif x is (len(str)-1):
                    print('Correct number1')

    elif str[0] is not '(':
        for x in range(len(str)):
            if str[x] is ')' or str[x] is '(':
                print('Invalid Numbe3')
                break
            elif str[len(str)-1] is str[x]:
                print('Correct number2')

elif k is 7:
    for x in range(len(str)):
            if str[x] is ')' or str[x] is '(':  #7 digit number does not have country code
                print('Invalid Numbe4')
                break
            elif str[len(str)-1] is str[x]:
                print('Correct number3')

else:
    print('Invalid Number4')



