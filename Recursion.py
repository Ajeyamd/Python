def first():
    second()
    print("first")
def second():
    third()
    print("second")
def third():
    fourth()
    print("third")
def fourth():
    print("fourth")
    
third()
