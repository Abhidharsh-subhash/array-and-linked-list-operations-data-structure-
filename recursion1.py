def Russiandoll(doll):
    if doll==1:
        print('all dolls are opened')
    else:
        print(doll)
        return Russiandoll(doll-1)

Russiandoll(5)