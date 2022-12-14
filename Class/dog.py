class Dog:
    """A simple attempt to simulate a dog"""

    def __init__(self, name, age) -> None:
        """" Initialize name and age attributes """
        self.name = name
        self.age = age
    

    def sit(self):
        """ Simulate a dog sitting in response to a command """
        print(f"{self.name} is now sitting.")

    
    def rol_over(self):
        """ Simulate a dog rolling over in response to a command """
        print(f"{self.name} rolled over!")


my_dog = Dog('willie', 6)

print(f"My dog`s name is {my_dog.name}")
print(f"My dog`s age is {my_dog.age} years old.")
