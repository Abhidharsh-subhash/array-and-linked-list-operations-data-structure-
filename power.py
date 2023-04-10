def power(base,exp):
    assert int(exp) == exp,'exponent must be an integer'
    if exp == 0:
        return 1
    elif exp<0:
        return 1/base * power(base,exp+1)
    else:
        return base*power(base,exp-1)

print(power(4,-1))