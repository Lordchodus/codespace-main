def save_user_data(data):
    """Saves user data to a file."""
    with open("user_data.txt", "a") as file:  # Open in append mode
        file.write(data + "\n")  # Add a newline for each entry

def load_user_data():
    """Loads user data from a file."""
    try:
        with open("user_data.txt", "r") as file:
            return [line.strip() for line in file]  # Read lines and remove newlines
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# Main program logic
if __name__ == "__main__":
    # Load previously saved data
    saved_inputs = load_user_data()
    if saved_inputs:
        print("Previously saved inputs:")
        for item in saved_inputs:
            print(f"- {item}")
    else:
        print("No previously saved inputs found.")

    # Get new input from the user
    new_input = input("Enter something to save (or 'quit' to exit): ")

    while new_input.lower() != 'quit':
        save_user_data(new_input)
        print(f"'{new_input}' saved.")
        new_input = input("Enter something else (or 'quit' to exit): ")

    print("Program exited.")