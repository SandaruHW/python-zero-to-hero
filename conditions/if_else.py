x = 160

if x >= 150:
    print("You are Selected!!")
else:
    print("You are not selected!!")


marks = 75

if marks > 50:
    result = "Pass"
else:
    result = "Fail"

print(result)


# 0 - 35 W
# 35 - 55 S
# 55 - 65 C
# 65 - 75 B
# 75 - 100 A

mark = -54

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


##Ternary operator
height = 165
job = "security" if height>150 else "labor"
print(job)