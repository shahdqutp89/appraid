def factorial(n):
    # If the number is less than or equal to 1, return 1 (base case)
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# Get user input
number = int(input("Enter a number to calculate its factorial: "))

# Call the factorial function and display the result
print(f"The factorial of {number} is: {factorial(number)}")
