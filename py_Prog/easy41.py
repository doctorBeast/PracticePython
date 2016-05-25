def prin_str(string):
    for _ in range(len(string)+6):
        print('*',end='')

    print('\n*',end='')

    for _ in range(len(string)+4):
        print(' ',end='')

    print('*\n*  '+string+'  *\n*',end='')

    for _ in range(len(string)+4):
        print(' ',end='')

    print('*\n',end='')

    for _ in range(len(string)+6):
        print('*',end='')

    print('\n\n',end='')

stri = input('Enter the string - ')

m = int(len(stri)/28)
for i in range(m+1):
    prin_str(stri[28*i:28*(i+1)])