# Instructions:

# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

# Step 1: Create Cat Objects

# Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat

# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

# Step 3: Print the Oldest Cat’s Details

# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Miti", 7)
cat2 = Cat("Pufi", 3)
cat3 = Cat("Luna", 5)


def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1  
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# Instructions:

# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class

# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “ goes woof!”.
# Create a jump() method that prints “ jumps cm high!”, where x is height * 2.

# Step 2: Create Dog Objects

# Create davids_dog and sarahs_dog objects with their respective names and heights.

# Step 3: Print Dog Details and Call Methods

# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

# Step 4: Compare Dog Sizes

class Dog:
    def __init__(self, dog_name, dog_height):
       self.name = dog_name
       self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")

davids_dog = Dog ("Rex",8)
sarahs_dog = Dog ("Sasha",5)

print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
else:
    print(f"{sarahs_dog.name} is bigger.")



# Instructions:

# Create a Song class with a method to print song lyrics line by line.

# Step 1: Create the Song Class

# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

class Song:
    def __init__(self, lyrics):
       self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line) 

my_song = Song(["Oh, my Darling", "I miss you", "All the stars into your eyes"])
my_song.sing_me_a_song()


# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.

# 2. Implement the __init__() method:

# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
# 3. Add a method add_animal(new_animal):

# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.
# 4. Add a method get_animals():

# This method prints all animals currently in the zoo.
# 5. Add a method sell_animal(animal_sold):

# This method checks if a specified animal exists on the animals list and if so, remove from it.
# 6. Add a method sort_animals():

# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
# 7. Add a method get_groups():

# This method prints the grouped animals as created by sort_animals().
# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.

class Zoo:
    def __init__(self, zoo_name: str):
        self.name = zoo_name
        self.animals = []              
        self._groups = {}              

    def add_animal(self, new_animal: str):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        """Print all animals in zoo."""
        if not self.animals:
            print("No animals in the zoo yet.")
            return
        print(f"Animals in {self.name}:")
        for a in self.animals:
            print(f" - {a}")

    def sell_animal(self, animal_sold: str):
       
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"Sold: {animal_sold}")
        else:
            print(f"{animal_sold} not found. Nothing sold.")

    def sort_animals(self):
       
        self.animals.sort()

        groups = {}
        for animal in self.animals:
            if not animal:  
                continue
            letter = animal[0].upper()
            groups.setdefault(letter, []).append(animal)

        self._groups = groups
        return self._groups

    def get_groups(self):
        
        if not self._groups:
            self.sort_animals()

        for letter in sorted(self._groups.keys()):
            print(f"{letter}: {self._groups[letter]}")

brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Giraffe")   # no double animal

brooklyn_safari.get_animals()
# -> Animals in Brooklyn Safari:
#    - Giraffe
#    - Bear
#    - Baboon

brooklyn_safari.sell_animal("Bear")
# -> Sold: Bear

brooklyn_safari.get_animals()
# -> Animals in Brooklyn Safari:
#    - Giraffe
#    - Baboon

grouped = brooklyn_safari.sort_animals()
print(grouped)
# -> {'B': ['Baboon'], 'G': ['Giraffe']}

brooklyn_safari.get_groups()
# -> B: ['Baboon']
#    G: ['Giraffe']
