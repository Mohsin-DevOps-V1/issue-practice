def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    The list must contain only numerical values.
    """
    total = 0
    # There is a bug in this for-loop.
    for number in numbers:
        total = total + number
        
    # The final division is also wrong.
    average = total / len(numbers)
    return average

# Example usage
data = [10, 20, 30, 40, 50]
result = calculate_average(data)
print(f"The average of the numbers is: {result}")

# The user reports this example not working as expected.
data_with_zero = [1, 2, 3, 4]
result_with_zero = calculate_average(data_with_zero)
print(f"The average of the numbers is: {result_with_zero}")
