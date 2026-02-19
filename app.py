import os
import sys
import json
import math
import random  # LINTING: unused import

# SYNTAX BUG: missing colon on function def
def calculate_area(radius)
    return math.pi * radius * radius


# TYPE_ERROR BUG: wrong type operation
def greet_user(name):
    age = "25"
    result = age + 5  # TypeError: can't add str + int
    return f"Hello {name}, you are {result} years old"


# LOGIC BUG: wrong comparison (should be >, not <)
def is_adult(age):
    if age < 18:
        return True   # Logic error: returns True for minors
    return False


# LINTING BUG: undefined variable used
def get_config():
    return config_data  # NameError: config_data not defined


# SYNTAX BUG: missing closing parenthesis
def add_numbers(a, b):
    return (a + b


class Calculator:
    def __init__(self):
        self.history = []

    def divide(self, a, b):
        # LOGIC BUG: no zero division check
        return a / b

    def square_root(self, n):
        return math.sqrt(n)
