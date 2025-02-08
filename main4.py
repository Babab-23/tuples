from functools import reduce

def multiply_tuple_elements(numbers):
    """Returns the product of all elements in the given tuple."""
    return reduce(lambda x, y: x * y, numbers)

# Example usage
tuple_numbers = (2, 3, 4, 5)
result = multiply_tuple_elements(tuple_numbers)
print("Product of tuple elements:", result)
