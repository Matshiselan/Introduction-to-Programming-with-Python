def main():
    x = int(input("Enter an number: "))
    is_even_result = is_even(x)
    if is_even_result:
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")

def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    main()