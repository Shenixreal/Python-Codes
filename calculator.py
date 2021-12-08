#addition
def add(num1, num2):
    return num1 + num2

#substraction
def substract(num1, num2):
    return num1 - num2

#multiplication
def multiply(num1, num2):
    return num1 * num2

#division
def divide(num1, num2):
    return num1 / num2

while True:

    print("\nPlease select an operation - \n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

    #select_the_operation
    choice = int(input("Choose an operation form: "))

    #user_input

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(num1, "+", num2, "=",
        add(num1, num2))

    elif choice == 2:
        print(num1, "-", num2, "=",
        substract(num1, num2))

    elif choice == 3:
        print(num1, "*", num2, "=",
        multiply(num1, num2))

    elif choice == 4:
        print(num1, "/", num2, "=",
        divide(num1, num2))

    else:
        print("Invalid input")

    repeat = input("\nDo you want another claculation? (y/n): ")
    if repeat == "n":
        break