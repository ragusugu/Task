class Person:
    # Constructor to initialize the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to print a greeting
    def greet(self):
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("John Doe", 25)

# Accessing attributes
print("Name:", person1.name)
print("Age:", person1.age)

# Calling the greet method
person1.greet()
