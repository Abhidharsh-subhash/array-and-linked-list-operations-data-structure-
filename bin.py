def bin(a):
    assert int(a) == a,'it must be an integer'
    if a==0:
        return 0
    else:
        return a%2 + 10 * bin(int(a/2))
    
print(bin(1.2))