# names = input('Whats your full name?: ')

# file = open('names.txt', 'a')
# file.write(f'{names}\n')
# file.close()

# Using 'with' statement to handle file operations
# with open('names.txt', 'a') as file:
#     file.write(f'{names}\n')

# reading the file and printing each name capitalized
names_list = []
with open('names.txt', 'r') as file:
    # lines = file.readlines()
    for line in file:
        names_list.append(line.strip().title())

for name in sorted(names_list):
    print(f'hello, {name}')