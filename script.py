# Function with a bug
def add_numbers(a, b):
    # This function is supposed to add two numbers, but it has a bug.
    # It will fail with a TypeError if one of the inputs is not an integer.
    return int(a) + int(b)

# Example usage
# This will work as expected
print(f"2 + 3 = {add_numbers(2, 3)}")

# This call will cause a bug and crash the script
print(f"5 + '10' = {add_numbers(5, '10')}")
