class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.year = year
        self.model = model

    def displayInfo(self):
        print(f"Brand: {self.brand}, Model:{self.model}, Year:{self.year}")


car1 = Car("Toyota", "Vios", "2004")
car1.displayInfo()