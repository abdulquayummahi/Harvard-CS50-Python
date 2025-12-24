def main():
    x = float(input("What is X: "))
    print(f"x squared is: {square(x)}")

def square(x):
    return x + x

if __name__ == "__main__":
    main()