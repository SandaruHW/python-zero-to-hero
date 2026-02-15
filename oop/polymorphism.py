class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound():
        return "Some generic sound"
    

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name, species = "Dog")
        self.breed = breed
        