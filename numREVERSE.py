def reverse(n):
    if len(n) in [0,1]:
        return n
    else:
        return n[len(n)-1] + reverse(n[:len(n)-1])
s='12345'
print(reverse(s))