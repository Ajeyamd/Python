def digit(n):
    if n in[0,9]:
        return n
    else:
        return digit((n//10))+(n%10)
print(digit(135785))
