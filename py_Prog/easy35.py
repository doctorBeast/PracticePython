def tripatt(num):
    j=1
    seq = {}
    i=1
    while i<(num+1):
        for k in range(j):
            if j in seq:
                seq[j]=seq[j]+' '+str(i)
                i+=1
                if i>num:
                    break
            else:
                seq[j]=str(i)
                i+=1
                if i>num:
                    break
        j+=1

    for i in range(1,len(seq)+1):
        seq[i]=seq[i].split()

    if len(seq[len(seq)-1])>= len(seq[len(seq)]):
        del seq[len(seq)]

    for i in range(len(seq)):
        print(' '.join(seq[len(seq)-i]),'\n')

tripatt(16)
