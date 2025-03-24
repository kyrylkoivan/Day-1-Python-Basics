# exception_practice.py

# 1. FileNotFoundError: Attempting to open a non-existent file
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")  # Handling file not found error

# 2. ZeroDivisionError: Attempting to divide by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Handling division by zero

# 3. IndexError: Accessing an out-of-range list index
my_list = [1, 2, 3]
try:
    print(my_list[5])  # Index out of range
except IndexError as e:
    print(f"Error: {e}")  # Handling index error

# 4. KeyError: Accessing a non-existent dictionary key
my_dict = {"name": "Alice", "age": 25}
try:
    print(my_dict["address"])  # Key does not exist
except KeyError as e:
    print(f"Error: {e}")  # Handling missing key

# 5. ValueError: Converting an invalid string to an integer
try:
    num = int("Hello")  # Invalid integer conversion
except ValueError as e:
    print(f"Error: {e}")  # Handling value error
