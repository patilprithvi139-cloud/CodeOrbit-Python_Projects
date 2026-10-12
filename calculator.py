def calculator():
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        choice = input("Choose an operation (1-5): ")
        if choice == "5":
            print("Thank you for using the calculator!")
            break
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select 1 to 5.")
            continue
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
        if choice == "1":
            result = num1 + num2
            print("Result:", result)
        elif choice == "2":
            result = num1 - num2
            print("Result:", result)
        elif choice == "3":
            result = num1 * num2
            print("Result:", result)

        elif choice == "4":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Result:", result)
if __name__ == "__main__":
    calculator()