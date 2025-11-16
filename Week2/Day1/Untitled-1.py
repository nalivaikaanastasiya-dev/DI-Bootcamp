class Dog():
    def __init__(self, name, color, breed, age, is_trained):
        self.name= name
        self.color = color
        self.breed = breed
        self.age = age
        self.is_trained = is_trained

dog1 = Dog('Rex', 'black', 'german shepherd', 8, True)
print(dog1)

print(dog1.name)
print(dog1.color)
print(dog1.breed)
print(dog1.age)
print(dog1.is_trained)
