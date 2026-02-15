class Dog:

    name = ""
    breed = ""

    def set_name(self, name):
        self.name =name
    
    def bark(self, message):
        print("Barking....", message)

    def walk(self):
        print("Walking...")


dog1 = Dog()

dog1.set_name("Scooby")
print(dog1.name)

dog2 = Dog()

dog2.set_name("Droofy")
print(dog2.name)