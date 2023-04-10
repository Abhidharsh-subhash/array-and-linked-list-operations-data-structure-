def palindrome(number):
    n=number
    rem=0
    revnum=0
    while number>0:
        rem=number%10
        revnum=(revnum*10)+rem
        number=number//10
    if n==revnum:
        return True
    else:
        return False
    

print(palindrome(121))