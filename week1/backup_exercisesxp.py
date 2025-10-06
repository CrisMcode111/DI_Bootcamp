# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
# Lists:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)

# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

# Family Data:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

# Bonus:

# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
        print(f"{name.title()} (age {age}) => Free")
    elif 3 <= age <= 12:
        price = 10
        print(f"{name.title()} (age {age}) => $10")
    else:
        price = 15
        print(f"{name.title()} (age {age}) => $15")
    total_cost += price

print(f"\nTotal cost for the family: ${total_cost}")

# Create and manipulate a dictionary that contains information about the Zara brand.

# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print(f"Zara’s clients are {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    del brand["creation_date"]

    print("Last international competitor:", brand["international_competitors"][-1])
    print("Major colors in the US:", brand["major_color"]["US"])
    print("Number of keys in dictionary:", len(brand))
    print("All keys in dictionary:", list(brand.keys()))
    print("\nFinal dictionary:", brand)

# Step 1: Define a Function with Parameters

# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.

# Step 2: Print a Message

# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.

# Step 3: Call the Function

# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").

# Expected Output:

# Reykjavik is in Iceland.
# Paris is in Unknown.

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Tokyo", "Japan")

# Goal: Create a function that generates random numbers and compares them.

# Key Python Topics:

# random module
# random.randint() function
# Conditional statements (if, else)

# Step 1: Import the random Module

# At the beginning of your script, use import random to access the random number generation functions.

# Step 2: Define a Function with a Parameter

# Create a function that accepts a number between 1 and 100 as a parameter.

# Step 3: Generate a Random Number

# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.

# Step 4: Compare the Numbers

# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.


# Step 5: Call the Function

# Call the function with a number between 1 and 100.

# Expected Output:

# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)

import random   


def compare_numbers(user_number):

    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Success! 🎉")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

compare_numbers(50) 

# Goal: Create a function to describe a shirt’s size and message, with default values.

# Step 1: Define a Function with Parameters

# Define a function called make_shirt().
# This function should accept two parameters: size and text.


# Step 2: Print a Summary Message

# Set up the function to display a sentence summarizing the shirt’s size and message.

# Step 3: Call the Function

# Step 4: Modify the Function with Default Values

# Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.

# Step 5: Call the Function with Default and Custom Values

# Call make_shirt() to make a large shirt with the default message.
# Call make_shirt() to make a medium shirt with the default message.
# Call make_shirt() to make a shirt of any size with a different message.

# Step 6 (Bonus): Keyword Arguments

# Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).

# Expected Output:

# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.

def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is '{text}'.")
make_shirt("large", "I love Python")
make_shirt("medium", "Code Everyday")
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")
make_shirt()                        
make_shirt("medium")                 
make_shirt("small", "Custom message")  

make_shirt(size="small", text="Hello!")
make_shirt(text="Keep Calm and Code", size="XL")


# Goal: Generate a random temperature and provide advice based on the temperature range.

# Step 1: Create the get_random_temp() Function

# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.


# Step 2: Create the main() Function

# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”


# Step 3: Provide Temperature-Based Advice

# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”


# Step 4: Floating-Point Temperatures (Bonus)

# Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.


# Step 5: Month-Based Seasons (Bonus)

# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.

# Expected Output

# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.


import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("Nice weather.")
    elif 23 <= temp < 32:
        print("A bit warm,stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

main()

def get_random_temp():
    return round(random.uniform(-10, 40), 1)

def get_random_temp(month):
    if month in [12, 1, 2]:  # iarnă
        return round(random.uniform(-10, 10), 1)
    elif month in [3, 4, 5]:  # primăvară
        return round(random.uniform(5, 20), 1)
    elif month in [6, 7, 8]:  # vară
        return round(random.uniform(20, 40), 1)
    elif month in [9, 10, 11]:  # toamnă
        return round(random.uniform(5, 25), 1)
    else:
        return round(random.uniform(-10, 40), 1)  # fallback
        

def main():
    month = int(input("Enter a month number (1-12): "))
    temp = get_random_temp(month)
    print(f"The temperature right now is {temp}°C.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("Nice weather.")
    elif 23 <= temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

main()

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.


toppings = []

print("Welcome to Python Pizza! 🍕")
print("Enter your toppings one by one. Type 'quit' when you're done.\n")

while True:
    topping = input("Enter a topping (or 'quit' to finish): ")

    if topping.lower() == "quit":
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")


base_price = 10
topping_price = 2.5
total_cost = base_price + topping_price * len(toppings)

print("\nYour pizza is ready! 🍽️")
print("Toppings:", ", ".join(toppings) if toppings else "No extra toppings")
print(f"Total cost: ${total_cost:.2f}")

