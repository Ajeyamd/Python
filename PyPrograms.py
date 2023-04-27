
def opendoll(doll):
    if doll==1:
        print("All dolls are opened")
    else:
        print(opendoll(doll-9))
