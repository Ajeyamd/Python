def power(n):
    if n==0:
        return 1
    else:
        p=power(n-1)
    return p*2
print(power(7))