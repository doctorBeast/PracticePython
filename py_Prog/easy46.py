import re

a = int(input('Enter the number :'))
a= bin(a)
new_a=str(a)
st = re.findall("(.)",new_a)

st[:2]=[]
print("The population of bit string is",st.count('1'))
