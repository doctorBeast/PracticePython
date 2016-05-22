'''
This is a generalized program .
It works with any random number of lockers and students.
'''

def togg(stud):
    global info
    global num_lock
    global num_stud

    while True:
        i=1
        while stud*i<=num_stud:
            info[stud*i]=info[stud*i]+'0'
            i+=1

        break

num_lock = int(input('What are the number of lockers: '))
num_stud = int(input('What are the number of students: '))
info = {}

for i in range(1,num_lock+1):
    info[i]='0'

for i in range(1,num_stud+1):
    togg(i)
total = 0
for i in range(1,num_lock+1):
    if len(info[i])%2>0:
        info[i]=1
    else:
        info[i]=0
        total+=1

'''
if the value in the dictionary corresponding to the locker is 1 then the locker is closed
else if it is 0 the the locker is open.
'''

print(total,'lockers are open')