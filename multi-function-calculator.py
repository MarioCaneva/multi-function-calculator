import math
import sympy
from sympy import symbols, solve, SympifyError

x = symbols('x')


# 1. Basic arithmetic
def basic_operations():
    print("\n--- Basic Operations ---")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero.")


# 2. Prime check
def is_prime():
    print("\n--- Prime Number Check ---")
    n = int(input("Enter an integer to check if it's prime: "))
    if n <= 1:
        print(n, "is not prime.")
        return
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(n, "is not prime.")
            return
    print(n, "is a prime number.")


# 3. Prime factorization
def prime_factors():
    print("\n--- Prime Factorization ---")
    n = int(input("Enter an integer to factor: "))
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print("Prime factors:", factors)


# 4. Simplify square roots
def simplify_square_root():
    print("\n--- Simplify Square Root ---")
    n = int(input("Enter a number to simplify its square root: "))
    outside = 1
    inside = n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % (i * i) == 0:
            outside = i
            inside = n // (i * i)
    if inside == 1:
        print(f"Simplified square root: {outside}")
    else:
        print(f"Simplified square root: {outside}√{inside}")


# 5. Solve equation for x
def solve_for_variable():
    print("\n--- Solve for x ---")
    eq = input('Enter an equation to solve for x (e.g., x**2 - 4): 0 = ')
    try:
        solutions = solve(eq, x)
        if len(solutions) == 0:
            print("No solution found.")
        else:
            print("Solutions for x:")
            for i, sol in enumerate(solutions):
                print(f"x{i+1} = {sol}")
    except SympifyError:
        print("Error: Could not parse equation.")
    except Exception as e:
        print("An error occurred:", e)


# 6. Convert decimal to fraction and percent
def decimal_to_fraction_percent():
    print("\n--- Convert Decimal to Fraction and Percent ---")
    digits = input("Enter a decimal number (e.g., 0.25): ")
    exponent = len(digits.split('.')[-1]) if '.' in digits else 0
    n = float(digits)
    numerator = int(float(digits) * (10 ** exponent))
    denominator = 10 ** exponent
    percent = n * 100
    print("The decimal is:", n)
    print("The fraction is:", numerator, "/", denominator)
    print("The percent is:", percent, "%")


# 7. Convert fraction to decimal and percent
def fraction_to_decimal_percent():
    print("\n--- Convert Fraction to Decimal and Percent ---")
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Error: denominator cannot be zero.")
        return
    decimal = numerator / denominator
    percent = decimal * 100
    print("Decimal:", decimal)
    print("Percent:", percent, "%")


# 8. Convert percent to decimal and fraction
def percent_to_decimal_fraction():
    print("\n--- Convert Percent to Decimal and Fraction ---")
    percent = float(input("Enter a percent (e.g., 25 for 25%): "))
    decimal = percent / 100
    numerator = int(percent)
    denominator = 100
    print("Decimal:", decimal)
    print("Fraction:", numerator, "/", denominator)


# 9. Solve proportions (new function!)
def solve_proportion():
    print("\n--- Solve a Proportion (a/b = c/x) ---")
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    c = float(input("Enter value for c: "))
    if a == 0:
        print("Error: Division by zero.")
        return
    x = (b * c) / a
    print(f"The value of x that solves {a}/{b} = {c}/x is x = {x}")


# 10. Exit function
def exit_calculator():
    print("\nThanks for using the algebra calculator. Goodbye!")
    return False


# Main menu loop
def main_menu():
    while True:
        print("\n===== Algebra Calculator Menu =====")
        print("1. Add, subtract, multiply, divide")
        print("2. Check if a number is prime")
        print("3. Generate prime factors")
        print("4. Simplify a square root")
        print("5. Solve for x in an equation")
        print("6. Convert decimal to fraction and percent")
        print("7. Convert fraction to decimal and percent")
        print("8. Convert percent to decimal and fraction")
        print("9. Solve proportions")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            basic_operations()
        elif choice == '2':
            is_prime()
        elif choice == '3':
            prime_factors()
        elif choice == '4':
            simplify_square_root()
        elif choice == '5':
            solve_for_variable()
        elif choice == '6':
            decimal_to_fraction_percent()
        elif choice == '7':
            fraction_to_decimal_percent()
        elif choice == '8':
            percent_to_decimal_fraction()
        elif choice == '9':
            solve_proportion()
        elif choice == '0':
            exit_calculator()
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

# Run the calculator
main_menu()
