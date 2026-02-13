#lists

x = [12, 434, 565, 77]

print(x)
print(x[0]) # 12
print(x[1]) # 434
#print(x[4]) # IndexError: list index out of range

x.append(100)
print(x) # [12, 434, 565, 77, 100]

x.insert(2, 200)
print(x) # [12, 434, 200, 565, 77, 100]

x.remove(434)
print(x) # [12, 200, 565, 77, 100]

x.pop(3)
print(x) # [12, 200, 565, 100]

y = [1, 2, 3]
z = x + y
print(z) # [12, 200, 565, 100, 1, 2, 3]

is_12_in_z = 12 in z
print(is_12_in_z) # True

is_200_not_in_z = 200 not in z
print(is_200_not_in_z) # False

