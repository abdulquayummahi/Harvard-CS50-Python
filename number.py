# x = int(input("Enter a number: "))
# print(f"X is: {x}")

# try:
#     x = int(input("Enter a number: "))
#     print(f"X is: {x}")
# except ValueError:
#     print("Please enter a number")
# else:
#     print(f"X is: {x}")


# def get_input():
#     try:
#         x = int(input("Enter a number: "))
#         print(f"X is: {x}")
#     except ValueError:
#         print("Please enter a number")
#         get_input()
#
# def main():
#     get_input()
#
# main()


# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Please enter a number")
#     # else:
#     #     print(f"X is: {x} (Inside loop)")
#     #     break
#
# print(f"X is: {x} (Out of loop)")


def main():
    x = get_int("Enter a number: ")
    print(f"X is: {x}")

def get_int(prompt):
    while True:
        try:
            # x = int(input("Enter a number: "))
            # return x
            return int(input(prompt))
        except ValueError:
            # print("Please enter a number")
            pass
        # else:
        #     break

main()