def first():
    second()
    print('first method')

def second():
    third()
    print('second method')

def third():
    four()
    print('third method')

def four():
    print('fourth method')


first()