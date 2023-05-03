def dec(n):
    assert int(n)==n,'Should be an Integer'
    if n==0:
        return 0
    else:
        return n%2 + 10*dec(int(n/2))
print(dec(1.3))
    