class Dog:
    pass


#object creation

dog1 = Dog()
dog1.name = "Scooby"

print(dog1.name)


class Cat:

    name = ""

    def sound(self):
        print("meow")

cat1 = Cat()
cat1.sound()
