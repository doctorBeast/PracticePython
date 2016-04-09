str1= input('Type the first string:')
str2= input('Type the second string:')

str1=list(str1)
str2=list(str2)

for i in range(len(str2)):
    str1.remove(str2[i])

str1=''.join(str1)
print(str1)