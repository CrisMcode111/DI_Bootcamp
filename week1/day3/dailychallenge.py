# Instructions: Old MacDonald’s Farm

# You are given example code and output. Your task is to create a Farm class that produces the same output.



# Step 1: Create the Farm Class

# Create a class called Farm.
# This class will represent a farm and its animals.

# Step 2: Implement the __init__ Method

# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes: name to store the farm’s name and animals to store the animals (initialize as an empty dictionary).

# Step 3: Implement the add_animal Method

# Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

# Step 4: Implement the get_info Method

# Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.

# Step 5: Test Your Code

# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.
# Bonus: Expand The Farm

# Step 6: Implement the get_animal_types Method

# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
# Use the sorted() function to sort the list.

# Step 7: Implement the get_short_info Method

# Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name if its count is greater than 1.
# Use string formatting to create the output.

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"

        info += "\n    E-I-E-I-O!"
        return info

def get_animal_types(self):
        return sorted(self.animals.keys())

def get_short_info(self):
        animal_types = self.get_animal_types()

        animals_list = []
        for animal in animal_types:
            count = self.animals[animal]
            if count > 1:
                animals_list.append(animal + "s")  # plural simplu
            else:
                animals_list.append(animal)

            if len(animals_list) > 1:
                animals_str= ", ".join(animals_list[:-1]) + " and " + animals_list[-1]
            else:
                animals_str = animals_list[0]

        return f"{self.name}'s farm has {animals_str}."