##
# COP1030 - Module A3 - Jason Kee
#

# Pounds
LIMIT_ONE = 2
LIMIT_TWO = 3.5
LIMIT_THREE = 7

# Prices
PRICE_ONE = 17.99
PRICE_TWO = 24.99
PRICE_THREE = 31.99
PRICE_FOUR = 49.99

# Tax and Subtotal
TAX = .0615
subtotal = 0

# Asking User for Name and Pounds
name = input("Please enter your name: ")
pounds = float(input("Please enter the pounds eaten: "))

# Calculate the Subtotal
if pounds < LIMIT_ONE:
    subtotal = PRICE_ONE
elif pounds <= LIMIT_TWO:
    subtotal = PRICE_TWO
elif pounds <= LIMIT_THREE:
    subtotal = PRICE_THREE
else:
    subtotal = PRICE_FOUR

# Calculate Tax and Total
taxAmount = subtotal * TAX
total = subtotal + taxAmount

# Output
print(f"Name: {name}")
print(f"Pounds Eaten: {pounds}")
print(f"Subtotal: {subtotal}")
print(f"Tax: {round(taxAmount, 2)}")
print(f"Total Due: {round(total, 2)}")