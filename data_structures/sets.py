x = {"Hello", "World", "Hello", "1"}

x.add("world")
print(x)

x.remove("1")
print(x)

##can't access by index

y = {"x", "y", "z", "1"}

z = x.union(y)
print(z)

z1 = x | y ##pipe operator is used for union of sets
print(z1)

z2 = x - y
print(z2)