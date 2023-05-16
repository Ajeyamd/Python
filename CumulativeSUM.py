def sum(a):
#     assert int(a)==a,'should be positive number'
    if a in [0,1]:
        return a
    else:
        return a+sum(a-1)
    
print(sum(15))