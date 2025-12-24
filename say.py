# import cowsay
import sys
from sayings import hello

# if len(sys.argv) == 2:
#     cowsay.cow("Hello, " + sys.argv[1])
    # cowsay.trex("Hello, " + sys.argv[1])

# cowsay.cow("Hello, " + sys.argv[1])

# for arg in sys.argv[1:]:
#     cowsay.cow("Hello, " + arg)
#     cowsay.trex("Hello, " + arg)

# cowsay.trex("Hello there, John")

if len(sys.argv) == 2:
    hello(sys.argv[1])