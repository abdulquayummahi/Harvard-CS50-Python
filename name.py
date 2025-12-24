import sys
# print("Hello my name is", sys.argv[0])

# try:
#     print("Hello my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# Check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too much arguments")
# else:
    # print("Hello my name is", sys.argv[1])

# Print name tags
# print("Hello my name is", sys.argv[1])

# for arg in sys.argv:
#     print("My name is: ", arg)

for arg in sys.argv[1:]:
    print("My name is: ", arg)