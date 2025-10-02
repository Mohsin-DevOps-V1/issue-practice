def add_numbers(a, b):
    try:
       return int(a) + int(b)
    except ValueError:
       return "Error: one of the inputs is not a number"
    except TypeError:
       return "Error: Invalid types passed"


print(f"2 + 3 = {add_numbers(2, 3)}")
print(f"5 + '10' = {add_numbers(5, '10')}")
print(f"5 + 'ten' = {add_numbers(5, 'ten')}")
