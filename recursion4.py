# def rec(n):
#     if n == 0:
#         return 1
#     else:
#         x = rec(n-1)
#         return x*2
    

def rec(n):
    i=0
    x=1
    while i<n:
        x=x*2
        i=i+1
    return x

print(rec(5))