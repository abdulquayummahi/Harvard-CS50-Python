# x = int(input("What is X: "))
#
# if x % 2 == 0:
#     print(f"X is even")
# else:
#     print(f"X is odd")


def main():
    x = int(input("What is X: "))

    if check_even(x):
        print(f"X is even")
    else:
        print(f"X is odd")

def check_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    # return True if num % 2 == 0 else False

    return num % 2 == 0

main()