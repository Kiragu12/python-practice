# Function to calculate factorial using a loop
def factorialloop(n):
    result = 1  
    for i in range(1, n + 1):  
        result =results * i  # Multiply result by each number
    return result

# Example test cases
print(factorial_loop(5))  # Output: 120

