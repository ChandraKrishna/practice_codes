# Swap two numbers without using a temporary variable
def swap_numbers(a, b):
    a, b = b, a
    return a, b

# Example usage:
num1 = 5
num2 = 10

print(f"Before swap: num1 = {num1}, num2 = {num2}")
num1, num2 = swap_numbers(num1, num2)
print(f"After swap: num1 = {num1}, num2 = {num2}")


# Swap two numbers using a temporary variable
def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Example usage:
num1 = 5
num2 = 10

print(f"Before swap: num1 = {num1}, num2 = {num2}")
num1, num2 = swap_numbers(num1, num2)
print(f"After swap: num1 = {num1}, num2 = {num2}")
