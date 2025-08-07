"""A simple calculator that prints the square of a user-provided number."""

def calculate(n: float) -> float:
    """Returns the square of a number."""
    return n * n

def main() -> None:
    """Main loop for user interaction."""
    print("Enter a number to see its square. Enter 'q' to quit.")
    while True:  # Fix: This needs to be indented inside main()
        user_input = input("What is x? ")
        if user_input.lower() == 'q':
            print("Goodbye")
            break
        try:
            x = float(user_input)
            print(f"x square is {calculate(x)}")
        except ValueError:
            print("Please enter a valid number or q to quit.")

if __name__ == "__main__":
    main()