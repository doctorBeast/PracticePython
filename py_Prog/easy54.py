'''
The strings have been appended by '?'
'''

def encode(stri,key):
    if len(stri)%key != 0:
        for _ in range(key-(len(stri)%key)):
            stri += '?'
    enc_str = ''
    for i in range(key):
        j=0
        while True:
            try:
                enc_str +=stri[i+j]
                j+=key
            except:
                break
    return enc_str



st = input("Enter the string :")
ke = int(input("Enter the key :"))

encoded = encode(st, ke)
print(encoded)

decoded = encode(encoded , int(len(encoded)/ke))
decoded = decoded.replace('?','')
print(decoded)