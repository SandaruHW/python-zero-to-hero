##tuple means a collection of items which is ordered and unchangeable. Tuples are written with round brackets.

sandaru = ("Sandaru", 22, "Sri Lanka", "Python Developer")

print(sandaru) # ('Sandaru', 22, 'Sri Lanka', 'Python Developer')
print(type(sandaru))

name = sandaru[0]
print(name) # Sandaru

print(sandaru.count('Sandaru')) # 1
print(sandaru.index('Python Developer')) # 3

