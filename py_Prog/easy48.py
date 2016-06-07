from array import array

arr = array('i',[1,2,3,4,7,53,61,44,2])
for i in arr:
    if i%2==0:
        arr.remove(i)
        arr.append(i)
    else:
        continue

arr.reverse()
print(arr)