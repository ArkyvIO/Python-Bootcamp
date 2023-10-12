#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Don't allow more symbols or numbers than there are characters in the password
if nr_letters < nr_symbols or nr_letters < nr_numbers:
    print("You entered a selection of more symbols or numbers than your password length. Defaulting to password length 16 with 2 numbers and 2 symbols.")
    nr_letters = 16
    nr_symbols = 2
    nr_numbers = 2

# Assign random letters to the password array for a beginning template, we will replace some indices with symbols and numbers
password = []
for x in range(nr_letters):
    password.append(random.choice(letters))

# Assign a random location for the symbols and the numbers
symbolLocs = [] # Create empty array to hold position values to place symbols in the password array
numberLocs = [] # Create empty array to hold position values to place numbers in the password array
while len(symbolLocs) < nr_symbols:
    possibleLocation = random.randint(0, nr_letters - 1)
    if possibleLocation not in symbolLocs and possibleLocation not in numberLocs:
        symbolLocs.append(possibleLocation)
while len(numberLocs) < nr_numbers:
    possibleLocation = random.randint(0, nr_letters - 1)
    if possibleLocation not in symbolLocs and possibleLocation not in numberLocs:
        numberLocs.append(possibleLocation)

# Assign symbols and numbers to the password using locations
for x in symbolLocs:
    password[x] = random.choice(symbols)
for x in numberLocs:
    password[x] = random.choice(numbers)

print("Your password is: " + "".join(password))