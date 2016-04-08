from itertools import permutations

text = input('Type a string:')

perms = [''.join(p) for p in permutations(text)]
print(perms)