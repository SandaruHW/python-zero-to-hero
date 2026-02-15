#access modfiers
#private

class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 25 #private

    def get_age(self):
        return self.__age

    def sleep(self):
        print(self.name,"Sleeping... ")


sandaru = Person("Sandaru")
sandaru.sleep()
print("Name is", sandaru.name)
print("Age is", sandaru.get_age())