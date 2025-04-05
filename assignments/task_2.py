''' Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
    1.  Takes a user's first name and last name as input.
    2.  Concatenates the first name and last name into a full name.
    3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like: '''


def create_greeting(first_name, last_name):
    try:
        full_name = f"{first_name} {last_name}"
        print(f"Hello, {full_name}! Welcome to the Python Program")
    except ValueError as e:
        print(f"Error: {e}")

# use main function
if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name  = input("Enter your last name: ")
    # Create and print personalized greeting
    create_greeting(first_name, last_name)

