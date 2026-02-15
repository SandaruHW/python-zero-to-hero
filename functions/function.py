def get_grade(mark):

    if mark<0 or mark>100:
        result1 = "Invalid marks"
    elif(mark>=0 and mark<35):
        result1 = "W"
    elif(mark<55):
        result1 = "S"
    elif(mark<65):
        result1 = "C"
    elif(mark<75):
        result1 = "B"
    else:
        result1 = "A"

    print(result1)

get_grade(75)
get_grade(-12)
get_grade(56)