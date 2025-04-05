'''' Task 1 : Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:

1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
    o	Addition
    o	Subtraction
    o	Multiplication
    o	Division
3.  Displays the results of each operation on the screen.

 Expected Output:
The output should include the result of each operation performed, for example: '''


def perform_arithmetic(number1, number2):
    try:
        result_addition         = number1 + number2
        result_subtraction      = number1 - number2
        result_multiplication   = number1 * number2
        result_division         = number1 / number2

        print(f"Addition        : {result_addition}")
        print(f"Subtraction     : {result_subtraction}")
        print(f"Multiplication  : {result_multiplication}")
        print(f"Division        : {result_division}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    perform_arithmetic(number1, number2)