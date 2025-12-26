# Ask the name
name = input('Whats your name? ')

# remove whitespace and capitalize
name = name.strip().title()

# Split into first and last name
first, last = name.split(' ')

# Greet the user
print(f'hello, {first}') 

