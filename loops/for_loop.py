x = [12,23,43,54,25]

index = 0

for item in x:

    if(item%2 == 0):
        continue

    y = x[index]
    print(index, item)
    index+=1


y = [12,23,567,123,88]

sum = 0
max = y[0]

for i in y:
    sum += i
    if(max<i):
        max = i
    

print("Summation of list:" , sum)
print("Maximum of list:", max)
print("Average of list:", sum/len(x))