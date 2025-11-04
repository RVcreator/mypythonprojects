while True:
    a = int(input("Input First Number: "))
    b = input("Input expression (+, -, *, /, %): ")
    c = int(input("Input Second Number: "))

    if b == "+":
        print(f"Your answer is: {a + c}")
    elif b == "-":
        print(f"Your answer is: {a - c}")
    elif b == "*":
        print(f"Your answer is: {a * c}")
    elif b == "/":
        print(f"Your answer is: {a / c}")
    elif b == "%":
        print(f"Your answer is: {a % c}")
    else:
        print("Invalid operator! Please use +, -, *, /, or %.")

    # ask if user wants to continue
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! 👋")
        break
