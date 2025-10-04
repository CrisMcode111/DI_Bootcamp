number = input("Tell me a number, please: ")
length = input("How long should the sequence be? ")

print("The number is:", number)
print("The length is:", length)

number = 2
length = 8

multiples = [number * i for i in range(1, length+1)]
print(multiples)



word = input("Please enter a word: ")

new_word = ""     
previous = ""    

for char in word:            
    if char != previous:      
        new_word += char     
        previous = char       


print("Result:", new_word)

