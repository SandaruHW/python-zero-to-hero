class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        return "Some generic sound"
    
class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name, species = "Dog")
        self.breed = breed

    def sound(self):
        return "Barking"
    
dog1 = Dog("Scooby", "Golden Retriever")
print(f"{dog1.name} is a {dog1.species} and it is {dog1.sound()}")