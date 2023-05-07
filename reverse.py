def reverse(a):
    if len(a) in [0,1]:
        return a
    else:
        return a[len(a)-1] + reverse(a[:len(a)-1])
s='admin'
print(reverse(s))