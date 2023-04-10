# to increase stack memory -->
# import sys
# sys.setrecursionlimit(5000)

def factorial(n):
    assert n>=0 and int(n)==n,'Only positive integer is allowed'
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(1))

