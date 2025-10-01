def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    The list must contain only numerical values.
    """
    if not numbers:
        return 0
        
    total = sum(numbers)
    
    average = total / len(numbers)
    return average

# Example usage
data =
result = calculate_average(data)
print(f"The average of the numbers is: {result}")

data_with_zero =
result_with_zero = calculate_average(data_with_zero)
print(f"The average of the numbers is: {result_with_zero}")

# Add a test case for the empty list to prove the fix
empty_data =
result_empty = calculate_average(empty_data)
print(f"The average of an empty list is: {result_empty}")

