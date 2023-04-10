def recursion(n):
    if n < 1:
        pass
    else:
        recursion(n-1)
        print(n)
        

recursion(4)