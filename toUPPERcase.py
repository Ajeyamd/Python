def capital(arr):
     if len(arr) == 0:
        return []
     else:
        return [arr[0].upper()]+capital(arr[1:])
    
print(capital(['hey','hello','bye']))