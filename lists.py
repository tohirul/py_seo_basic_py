actor = ["Tom Cruise", "Angelina Jolie", "Kristen Stewart"]
print(actor)
# include type checking for input


def add_actor(actor):
    # redo the following code with do while loop
    # actor = []
    while True:
        new = input("Enter an actor name: \n")
        if isinstance(new, str):
            actor.append(new)
            print(actor)
            break
        print("Please enter a string")
        continue


add_actor(actor)


def greet_actor(actor):
    for ac in actor:
        print(f"Hello {ac}")


greet_actor(actor)


fruits = ["apple", "banana", "cherry"]
print(fruits)


def add_fruit(fruits):
    while True:
        new = input("Enter a fruit name: \n")
        if isinstance(new, str):
            fruits.append(new)
            print(fruits)
            break
        print("Please enter a string")
        continue


add_fruit(fruits)


def add_to_index(fruits):
    while True:
        index = int(input("Enter the index: \n"))
        if index < 0 or index > len(fruits):
            print("Invalid index")
            continue
        new = input("Enter a fruit name: \n")
        if isinstance(new, str):
            fruits.insert(index, new)
            print(fruits)
            break
        print("Please enter a string")
        continue


add_to_index(fruits)
