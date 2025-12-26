def main():
    x = get_integer(prompt='Enter an integer: ')
    print(f'You entered: {x}')


def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Input must be an integer')
        else:
            return value

if __name__ == '__main__':
    main()
