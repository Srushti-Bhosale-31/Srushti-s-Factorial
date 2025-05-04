# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate the factorial of 5
num = 5
result = factorial(num)

# Print the result
print(f"The factorial of {num} is: {result}")
