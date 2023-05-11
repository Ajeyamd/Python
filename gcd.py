def gcd(a,b):
    assert int(a)==a and int(b)==b,'Integers should be positive'
    if a==0:
        return b
    if b==0:
        return a 
    else:
        return gcd(b,a%b)
print(gcd(-48,18))