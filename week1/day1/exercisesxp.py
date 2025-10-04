# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

for i in range(4):
    print("Hello world")

# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).


result = (99 ** 3) * 8
print(result)


# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.


my_name = "Cristina"
name = input ("What's your name,")
if name == my_name:
   print("You are a princess")
else:
   print("I don't like you")


#    Exercise 4 : Tall enough to ride a roller coaster
# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height = 145
if height >= 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride!")


#     Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {2,4,6}
my_fav_numbers.add(8)
my_fav_numbers.remove(8)
friend_fav_numbers = {1,3,5}
our_fav_numbers = my_fav_numbers and friend_fav_numbers

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
my_tuple = (1,2,3)
print(type(my_tuple))

my_tuple = (*my_tuple,4,5,6)
print(my_tuple)

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)

basket.count("Apples")
print(basket.count("Apples"))

basket.clear()
print(basket.clear())


# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"].

# The deli has run out of pastrami, use a while loop to remove all occurrences of Pastrami sandwich from sandwich_orders.
# We need to prepare the orders of the clients:

# Create an empty list called finished_sandwiches.

# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:


# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich


sandwich_orders = [
    "Tuna sandwich", 
    "Pastrami sandwich", 
    "Avocado sandwich", 
    "Pastrami sandwich", 
    "Egg sandwich", 
    "Chicken sandwich", 
    "Pastrami sandwich"
]

print("Sorry, we have run out of Pastrami today!")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches are ready:", finished_sandwiches)



