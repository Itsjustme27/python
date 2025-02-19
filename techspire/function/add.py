def sum(x,y):
    return x+y

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = sum(num1, num2)
    print(f"Sum of the given two numbers is: {result}")

if __name__ == "__main__":
    main()
