def sequence(n):
    total=0
    for i in range(n):
        total=total+sum(i,i+1) 
    return total

def sum(a,b):
    return a+b

print(sequence(4))