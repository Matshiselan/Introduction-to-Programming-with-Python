name = input("What is your name? ")

match name:
    case "Alice" | "Bob" | "Eve":
        print(f"Hello, {name}!")
    case "Charlie":
        print("Hey Charlie, long time no see!")
    case _:
        print("I don't know you.")