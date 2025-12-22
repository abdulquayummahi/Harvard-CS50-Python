# print("Hello World")

## Ask user for their name
# print("Hey,What is your name? \nAns:")
# name = input("Hey,What is your name? \nAns:")
# print(f"Hello, {name}")
# print("Hello, " + name)

# print("Hello,", name, end=f" end: {name}")
# print("Hello,", name, end="")

# print("Hello, \"friend\"")

# name = name.strip().title() # Removes whitespace and Caps all first letter
# name = name.capitalize() # First letter is capitalized
# name = name.title()
# print(f"Hello, {name.strip().title()}", end="")

# first, last = name.split(" ")
# print(f"Hello, {first}")

def main():
    name = input("Hey,What is your name? \nAns:")
    # hello()
    hello(name)
    # print(name)

    number = int(input("What is your number? "))
    print(f"Square of {number} is: {square(number)}")

def hello(to="World"):
    print(f"Hello, {to}")

def square(num=0):
    # return num * num
    # return num ** 2
    return pow(num, 2)

main()