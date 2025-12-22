# print("Meow")
# print("Meow")
# print("Meow")


# i = 0
# while i <= 2:
#     print("Meow")
#     i += 1 # i = i + 1


# i = 2
# while i>=0:
#     print("Meow")
#     i-=1 #i=i-1


# for i in [0, 1, 2]:
#     print("Meow")


# for i in range(3):
#     print("Meow")

# print("Meow\n" *3, end="")


# while True:
#     n = int(input("Enter a number: "))
#     if n > 0:
#         break
#
# for _ in range(n):
#     print("Meow")


def main():
    num = get_user_input()
    meow(num)

def get_user_input():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()