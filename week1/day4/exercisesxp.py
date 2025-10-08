# Instructions:

# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.

# Step 1: Create the Siamese Class

# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.

# Step 2: Create a List of Cat Instances

# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.

# Step 3: Create a Pets Instance

# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.

# Step 4: Take Cats for a Walk

# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.
# Step 1: Create the Siamese class

# Step 2: Create a list of cat instances

# Step 3: Create a Pets instance of the list of cat instances

# sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
# sara_pets.walk()

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{self.name} sings {sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{self.name} sings {sounds}'


# Step 1: Create the Siamese class
class Siamese(Cat):
    def sing(self, sounds):
        return f'{self.name} sings {sounds}'


# Step 2: Create a list of cat instances
bengal_cat = Bengal("Simba", 3)
chartreux_cat = Chartreux("Luna", 2)
siamese_cat = Siamese("Milo", 4)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()

# Instructions:

# Step 1: Create the Dog Class

# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “ is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.

# Step 2: Create Dog Instances

# Create three instances of the Dog class with different names, ages, and weights.

# Step 3: Test Dog Methods

# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"The fight between {self.name} and {other_dog.name} is a draw!"


# Step 2: Create Dog instances
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Bella", 3, 15)
dog3 = Dog("Max", 7, 30)

# Step 3: Test Dog methods
print(dog1.bark())
print(f"{dog2.name}'s run speed is {dog2.run_speed():.2f}")
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))


# Instructions:

# Step 1: Import the Dog Class

# In a new Python file, import the Dog class from the previous exercise.

# Step 2: Create the PetDog Class

# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “ all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a rendom index from it each time the method is called.

# Step 3: Test PetDog Methods

# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.


import random

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"The fight between {self.name} and {other_dog.name} is a draw!"

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        dog_names.append(self.name)
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll",
                      "stands on his back legs",
                      "shakes your hand",
                      "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")


dog1 = PetDog("Rex", 5, 20)
dog2 = PetDog("Bella", 3, 15)
dog3 = PetDog("Max", 7, 30)

dog1.train()            
dog1.play(dog2, dog3)    
dog1.do_a_trick()        

dog2.do_a_trick()


# Instructions:

# Step 1: Create the Person Class

# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.

# Step 2: Create the Family Class

# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)

# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.

# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."


# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.


class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""  

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []  

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name  
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("This person is not in the family.")

    def family_presentation(self):
        print(f"Family {self.last_name}")
        for member in self.members:
            print(f"- {member.first_name} ({member.age} years old)")


my_family = Family("Ionesco")

my_family.born("Ana", 16)
my_family.born("Ion", 20)
my_family.born("Maria", 12)

my_family.check_majority("Ana")
my_family.check_majority("Ion")

my_family.family_presentation()
