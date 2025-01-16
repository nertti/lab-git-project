def multiply_numbers(a, b):
    return a * b
def add_numbers(a, b):
    return a + b
def factorial(n):
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
