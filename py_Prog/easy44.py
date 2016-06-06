import re
import operator

fip = open("actual.txt",'r')
stri = re.findall("(.*)",fip.read())#this statement helps in removing all the '\n' from the data
a=[x for x in stri if x !='']
newstri = " ".join(a)
new = re.findall("(.*?)[.?!]",newstri)#selecting the different sentences
fip.close()
for i in range(len(new)):#for removing "  ',:;   " characters because they are not the part of a word
    lis = re.findall("([A-Za-z ]+)",new[i])
    new[i] = "".join(lis)

dic={}
for line in new:# assigning number of words in each sentence
    lis = line.split()
    dic[line] = len(lis)


longest = []
a = sorted(dic.items(), key = operator.itemgetter(1), reverse=True)
for ele in a:#useful if there are more than one sentece with most words
    if ele[1] == a[0][1]:
        longest.append(ele[0])
    else:
        break

print("The most number of words are", a[0][1]," and the sentences are :")
for i in range (len(longest)):
    print(str(i+1)+".", longest[i])

i=1
for line in longest:# printing the words with length greater than 4
    print("The words in sentence",i,"with length greater than 4 :")
    words_long = line.split()
    for word in words_long:
        if len(word)> 4:
            print (word)
        else:
            continue
    i+=1
