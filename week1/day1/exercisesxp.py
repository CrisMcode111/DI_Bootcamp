for i in range(4):
    print("Hello world")

result = (99 ** 3) * 8
print(result)

my_name = "Cristina"
name = input ("What's your name,")
if name == my_name:
   print("You are a princess")
else:
   print("I don't like you")

height = 145
if height >= 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride!")

my_fav_numbers = {2,4,6}
my_fav_numbers.add(8)
my_fav_numbers.remove(8)
friend_fav_numbers = {1,3,5}
our_fav_numbers = my_fav_numbers and friend_fav_numbers


my_tuple = (1,2,3)
print(type(my_tuple))

my_tuple = (*my_tuple,4,5,6)
print(my_tuple)


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



