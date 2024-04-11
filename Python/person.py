# Define the Person class
class Person:
    # Constructor method to initialize name, age, and gender attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to introduce the person
    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Create an instance of the Person class
person1 = Person("John Doe", 30, "Male")

# Call the introduce method
person1.introduce()