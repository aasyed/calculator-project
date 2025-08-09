"""A simple calculator that prints the square of a user-provided number."""

def calculate(n: float) -> float:  
    """Returns the square of a number."""
    return n * n  # Multiply the number by itself to get the square

def display_welcome() -> None: 
    """Display welcome message and instructions."""
    print("=" * 40)  # Print a decorative line of 40 equal signs
    print("    SQUARE CALCULATOR")  # Print the title with spacing for centering
    print("=" * 40)  # Print another decorative line of 40 equal signs
    print("Enter a number to see its square.")  # Display user instruction
    print("Type 'q' to quit.")  # Display quit instruction
    print("-" * 40)  # Print a separator line of 40 dashes

def main() -> None:  # Main function to run the calculator
    """Main loop for user interaction."""
    display_welcome()  # Call function to show welcome message and instructions
    
    while True:  # Start infinite loop until user chooses to quit
        user_input = input("\nWhat is x? ").strip()  # Get user input and remove whitespace
        
        if user_input.lower() == 'q':  # Check if user wants to quit (case-insensitive)
            print("\nGoodbye! 👋")  # Display farewell message with emoji
            break  # Exit the while loop and end the program
            
        try:  # Start error handling block for invalid input
            x = float(user_input)  # Attempt to convert user input to a float number
            result = calculate(x)  # Call calculate function to get the square
            print(f"✅ The square of {x} is {result}")  # Display result with checkmark emoji
        except ValueError:  # Handle error if input cannot be converted to float
            print("❌ Please enter a valid number or 'q' to quit.")  # Show error message with X emoji

if __name__ == "__main__":  # Check if script is run directly (not imported)
    main()  # Call the main function to start the program
    
