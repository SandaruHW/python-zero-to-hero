count = 0

while True:

    print(count)
    count+=1

    if(count == 10):
        break


x = [12, 43, 67, 356, 76, 45]

max = x[0]
min = x[0]
i=0

while i<len(x):

    if(max < x[i]):
        max = x[i]

    if(min > x[i]):
        min = x[i]
    
    i += 1

print(max)
print(min)
