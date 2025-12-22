# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

# def main():
#     print_column(3)
#
# def print_column(height):
#     for row in range(height):
#         # print("#")
#         print("#\n" * height, end="")
#
# main()

# def main():
#     print_row(4)
#
# def print_row(row):
#     print("?" * row)
#
# main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        # for j in range(size):
        #     print("#", end="")
        # print()
        print_row(size)

def print_row(width):
    print("#" * width)

main()