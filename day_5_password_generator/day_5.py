# Password Generator Project
from math import floor
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

####
# Random letters
####
random_letters = []
for number_of_letter in range(1, nr_letters + 1):
    # print("working")
    # Get random index for random letters
    random_idx = floor(random.random() * len(letters))
    # print(random_idx)
    random_letter = letters[random_idx]
    # print(random_letter)
    random_letters.append(random_letter)
# print("".join(random_letters))

####
# Random symbols
####

random_symbols = []
for number_of_symbol in range(1, nr_symbols + 1):
    random_idx_symbol = floor(random.random() * len(symbols))
    random_symbol = symbols[random_idx_symbol]
    random_symbols.append(random_symbol)
# print("".join(random_symbols))

####
# Random numbers
####

random_numbers = []
for number_of_number in range(1, nr_numbers + 1):
    random_idx_number = floor(random.random() * len(numbers))
    random_number = numbers[random_idx_number]
    random_numbers.append(random_number)
# print("".join(random_numbers))

password = random_letters + random_symbols + random_numbers
join_password = "".join(password)

print(f"Here is your password: {join_password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password)
join_random_ordered_password = "".join(password)

print(f"Here is your password: {join_random_ordered_password}")
