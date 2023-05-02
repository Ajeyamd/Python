def power(n,p):
    assert n>=0 and int(n)==n,'Number should be positive'
    if p==0:
        return 1
    elif n==0:
        return 'not defined'
    else:
        t=n*power(n,p-1)
        return t
    
print(power(2,2))