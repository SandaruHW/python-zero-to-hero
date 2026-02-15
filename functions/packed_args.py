
#packed arguments
def get_total(*marks):

    print(type(marks))

    total = 0
    for i in marks:
        total += i
    
    print(total)


get_total(78,75,43)
print(type(get_total))


#keyword arguments

def my_form(**params):
    print(params)

my_form(name = "Sandaru", age = 24, city = "Amabalangoda")
my_form(name = "Sandaru", age = 24)