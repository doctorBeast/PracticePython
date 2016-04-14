month=['march','april','may','june','july','august','september','october','november','december','january','february']
cor_no=[1,2,3,4,5,6,7,8,9,10,11,12]
week=['Sunday','Monday','Tuseday','Wednesday','Thursday','Friday','Saturday']

d = int(input('What is the day?'))
m = input('What is the month?')
Y = int(input('What is the year?'))


m = m.lower()
for x in range(len(month)):
    if m == month[x]:
        m=cor_no[x]
        break

if m is 11 or m is 12:
    Y=Y-1

y=Y%100
c=Y/100

w=float(d+(2.6*m-0.2)+y+y/4+c/4-2*c)%7

print('The day on that day is ',week[int(w)])


