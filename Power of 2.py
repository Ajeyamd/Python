# def power(n):
#     i=0
#     power=1
#     while i<n:
#         power=power*2
#         i=i+1
#     return power
# print(power(3))

def power(n):
    if n==0:
        return 1
    else:
        p=power(n-1)
    return p*2
print(power(3))