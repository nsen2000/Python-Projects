import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_characters = nr_letters + nr_symbols + nr_numbers
password = []
let_check = 0
num_check = 0
sym_check = 0

for x in range(0, 50):
    randInt = random.randint(1, 3)
    if randInt == 1 and let_check < nr_letters:
        password.append(random.choice(letters))
        let_check += 1
    elif randInt == 2 and num_check < nr_numbers:
        password.append(random.choice(numbers))
        num_check += 1
    elif randInt == 3 and sym_check < nr_symbols:
        password.append(random.choice(symbols))
        sym_check += 1

print(nr_characters)
print(''.join(password))
k = input("press anything to exit")