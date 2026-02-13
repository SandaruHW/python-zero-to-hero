x = {'1000': "Colombo", '12500' : "Panadura"}

x['1200'] = "Moratuwa"
print(x) # {'1000': 'Colombo', '12500': 'Panadura', '1200': 'Moratuwa'}

print(x.keys()) # dict_keys(['1000', '12500', '1200'])
print(x.values()) # dict_values(['Colombo', 'Panadura', 'Moratuwa'])


y = x.get('12000', "Not Found")
print(y) # Not Found

del x['12500']
print(x) # {'1000': 'Colombo', '1200': 'Moratuwa'}


p = {
    "a": ['Hello', 'Hi', 'Good Morning'],
    "b": ['Bye', 'Good night'],
    "c": 16
}

print(p) # {'a': ['Hello', 'Hi', 'Good Morning'], 'b': ['Bye', 'Good night'], 'c': 16}

y = p["a"]
print(y) # ['Hello', 'Hi', 'Good Morning']

y.append("Good Afternoon")
print(y) # ['Hello', 'Hi', 'Good Morning', 'Good Afternoon']
