# @Author: Arif Kasim Rozani - (Team Operation Badar)
# Python Operators and Variables - Detailed Explanation with Examples

print("=" * 60)
print("PYTHON OPERATORS AND VARIABLES - COMPREHENSIVE GUIDE")
print("=" * 60)

# ============================================================================
# SECTION 1: OPERATOR AND OPERAND BASICS
# ============================================================================

print("\n🔹 SECTION 1: OPERATOR AND OPERAND BASICS")
print("-" * 50)

print("""
WHAT ARE OPERATORS AND OPERANDS?
- OPERATOR: A symbol that performs an operation (e.g., +, -, *, /)
- OPERAND: The value(s) or variable(s) that the operator works with

Think of it like a math equation: 5 + 3
- '+' is the OPERATOR
- '5' and '3' are the OPERANDS
""")

# Example of operators and operands
a = 10
b = 5
result = a + b  # 'a' and 'b' are operands, '+' is operator

print(f"Example: {a} + {b} = {result}")
print(f"Operands: {a}, {b}")
print(f"Operator: +")
print(f"Result: {result}")

# ============================================================================
# SECTION 2: UNARY OPERATORS (Work with ONE operand)
# ============================================================================

print("\n🔹 SECTION 2: UNARY OPERATORS")
print("-" * 50)

print("Unary operators work with ONE operand only:")

# 1. Negative (-) Operator
print("\n1. NEGATIVE (-) OPERATOR:")
x = 5
y = -x  # Changes sign
print(f"x = {x}")
print(f"y = -x = {y}")

# 2. Logical NOT (not) Operator
print("\n2. LOGICAL NOT (not) OPERATOR:")
is_sunny = True
is_cloudy = not is_sunny  # Reverses boolean
print(f"is_sunny = {is_sunny}")
print(f"is_cloudy = not is_sunny = {is_cloudy}")

# 3. Bitwise NOT (~) Operator
print("\n3. BITWISE NOT (~) OPERATOR:")
num = 5  # Binary: 0101
inverted = ~num  # Inverts all bits
print(f"num = {num} (binary: {bin(num)})")
print(f"~num = {inverted}")
print(f"Binary representation of {num}: {format(num, 'b')}")

# ============================================================================
# SECTION 3: BINARY OPERATORS (Work with TWO operands)
# ============================================================================

print("\n🔹 SECTION 3: BINARY OPERATORS")
print("-" * 50)

print("Binary operators work with TWO operands:")

# Examples will be shown in detail in the following sections

# ============================================================================
# SECTION 4: ARITHMETIC OPERATORS
# ============================================================================

print("\n🔹 SECTION 4: ARITHMETIC OPERATORS")
print("-" * 50)

print("Used for basic mathematical operations:")

a = 10
b = 3

print(f"\nUsing a = {a} and b = {b}:")
print(f"a + b  = {a + b}   (Addition)")
print(f"a - b  = {a - b}   (Subtraction)")
print(f"a * b  = {a * b}   (Multiplication)")
print(f"a / b  = {a / b}   (Division - returns float)")
print(f"a // b = {a // b}  (Floor Division - removes decimal)")
print(f"a % b  = {a % b}   (Modulus - remainder)")
print(f"a ** b = {a ** b}  (Exponentiation - a to the power of b)")

# Real-world example
print("\n📝 REAL-WORLD EXAMPLE:")
total_items = 17
items_per_box = 5
full_boxes = total_items // items_per_box
remaining_items = total_items % items_per_box

print(f"If you have {total_items} items and each box holds {items_per_box} items:")
print(f"You can fill {full_boxes} complete boxes")
print(f"With {remaining_items} items left over")

# ============================================================================
# SECTION 5: COMPARISON (RELATIONAL) OPERATORS
# ============================================================================

print("\n🔹 SECTION 5: COMPARISON OPERATORS")
print("-" * 50)

print("Used to compare two values - always return True or False:")

x = 10
y = 5

print(f"\nUsing x = {x} and y = {y}:")
print(f"x == y  = {x == y}  (Equal to)")
print(f"x != y  = {x != y}  (Not equal to)")
print(f"x > y   = {x > y}   (Greater than)")
print(f"x < y   = {x < y}   (Less than)")
print(f"x >= y  = {x >= y}  (Greater than or equal)")
print(f"x <= y  = {x <= y}  (Less than or equal)")

# Chained Comparison Example
print("\n📝 CHAINED COMPARISON EXAMPLE:")
age = 25
if 18 <= age <= 65:
    print(f"Age {age} is in working range (18-65)")
else:
    print(f"Age {age} is outside working range")

# This is equivalent to: 18 <= age and age <= 65

# ============================================================================
# SECTION 6: LOGICAL OPERATORS
# ============================================================================

print("\n🔹 SECTION 6: LOGICAL OPERATORS")
print("-" * 50)

print("Used to combine conditional statements:")

x = True
y = False

print(f"\nUsing x = {x} and y = {y}:")
print(f"x and y = {x and y}  (Both must be True)")
print(f"x or y  = {x or y}   (At least one must be True)")
print(f"not x   = {not x}    (Opposite of x)")

# Real-world example
print("\n📝 REAL-WORLD EXAMPLE:")
has_license = True
is_over_18 = True
can_drive = has_license and is_over_18

print(f"Has license: {has_license}")
print(f"Is over 18: {is_over_18}")
print(f"Can drive: {can_drive}")

# ============================================================================
# SECTION 7: ASSIGNMENT OPERATORS
# ============================================================================

print("\n🔹 SECTION 7: ASSIGNMENT OPERATORS")
print("-" * 50)

print("Used to assign values to variables:")

# Basic assignment
x = 5
print(f"Assignment: x = 5                     → x = {x}")

# Addition assignment
x += 3  # Same as: x = x + 3
print(f"Addition Assignment: x += 3           → x = {x}")

# Subtraction assignment
x -= 2  # Same as: x = x - 2
print(f"Subtraction Assignment: x -= 2        → x = {x}")

# Multiplication assignment
x *= 3  # Same as: x = x * 3
print(f"Multiplication Assignment: x *= 3     → x = {x}")

# Division assignment
x /= 2  # Same as: x = x / 2
print(f"Division Assignment: x /= 2           → x = {x}")

# Floor division assignment
x //= 3  # Same as: x = x // 3
print(f"Floor Division Assignment: x //= 3    → x = {x}")

# ============================================================================
# SECTION 8: WALRUS OPERATOR (:=)
# ============================================================================

print("\n🔹 SECTION 8: WALRUS OPERATOR (:=)")
print("-" * 50)

print("The walrus operator := allows assignment and evaluation in one line:")

# Example 1: Input validation
print("\n📝 EXAMPLE 1: Input validation")
# Simulating user input for demonstration
user_input = "123"  # In real code, this would be input()

if (n := len(user_input)) > 2:
    print(f"Input '{user_input}' has {n} characters (more than 2)")
else:
    print(f"Input '{user_input}' has {n} characters (2 or less)")

# Example 2: Processing data
print("\n📝 EXAMPLE 2: Processing numbers")
numbers = [1, 2, 3, 4, 5]
if (total := sum(numbers)) > 10:
    print(f"Sum of {numbers} is {total} (greater than 10)")

# ============================================================================
# SECTION 9: IDENTITY OPERATORS
# ============================================================================

print("\n🔹 SECTION 9: IDENTITY OPERATORS")
print("-" * 50)

print("Used to compare memory locations (not just values):")

a = [1, 2, 3]
b = [1, 2, 3]  # Same values, different memory location
c = a          # Same memory location as 'a'

print(f"\na = {a}")
print(f"b = {b}")
print(f"c = a (c points to same memory as a)")

print(f"\na is c     = {a is c}       (Same object in memory)")
print(f"a is b     = {a is b}       (Different objects)")
print(f"a == b     = {a == b}       (Same values)")
print(f"a is not b = {a is not b}   (Different memory locations)")

print(f"\nMemory addresses:")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")

# ============================================================================
# SECTION 10: MEMBERSHIP OPERATORS
# ============================================================================

print("\n🔹 SECTION 10: MEMBERSHIP OPERATORS")
print("-" * 50)

print("Used to check if a value exists in a sequence:")

# Example with list
my_list = [1, 2, 3, 4, 5]
print(f"\nmy_list = {my_list}")
print(f"3 in my_list      = {3 in my_list}")
print(f"10 not in my_list = {10 not in my_list}")

# Example with string
my_string = "Operation Badar"
print(f"\nmy_string = '{my_string}'")
print(f"'O' in my_string          = {'O' in my_string}")
print(f"'Hello' not in my_string  = {'Hello' not in my_string}")

# Example with dictionary
my_dict = {"name": "Abdul", "age": 25}
print(f"\nmy_dict = {my_dict}")
print(f"'name' in my_dict = {'name' in my_dict}")
print(f"'city' in my_dict = {'city' in my_dict}")

# ============================================================================
# SECTION 11: PYTHON KEYWORDS
# ============================================================================

print("\n🔹 SECTION 11: PYTHON KEYWORDS")
print("-" * 50)

import keyword

print("Keywords are reserved words that have special meanings in Python.")
print("You CANNOT use them as variable names!")

print(f"\nTotal keywords in Python: {len(keyword.kwlist)}")
print("List of all keywords:")

# Print keywords in a formatted way
for i, kw in enumerate(keyword.kwlist, 1):
    print(f"{kw:10}", end="")
    if i % 6 == 0:  # New line every 6 keywords
        print()
print()  # Final newline

# Example of what happens if you try to use a keyword
print("\n❌ WRONG: Cannot use keywords as variable names")
print("# and = True  # This would cause a SyntaxError")

# ============================================================================
# SECTION 12: PYTHON VARIABLES
# ============================================================================

print("\n🔹 SECTION 12: PYTHON VARIABLES")
print("-" * 50)

print("Variables are containers for storing data values.")

# Variable assignment
name = "Abdul Rahman"
age = 25
height = 5.8
is_student = True

print(f"\nVariable examples:")
print(f"name = '{name}' (type: {type(name).__name__})")
print(f"age = {age} (type: {type(age).__name__})")
print(f"height = {height} (type: {type(height).__name__})")
print(f"is_student = {is_student} (type: {type(is_student).__name__})")

# ============================================================================
# SECTION 13: VARIABLE NAMING RULES
# ============================================================================

print("\n🔹 SECTION 13: VARIABLE NAMING RULES")
print("-" * 50)

print("""
RULES FOR NAMING VARIABLES:
1. Can contain letters, digits, and underscores (_)
2. Cannot start with a digit
3. Case-sensitive (myVar ≠ myvar)
4. Cannot use Python keywords
5. Cannot contain spaces or special characters (except _)
""")

# Valid variable names
print("✅ VALID variable names:")
user_name = "Abdul"
_age = 25
salary2024 = 50000
myVariable = "Python"

print("user_name, _age, salary2024, myVariable")

print("\n❌ INVALID variable names (would cause errors):")
print("2name, my-variable, class, for, if")

# ============================================================================
# SECTION 14: NAMING CONVENTIONS
# ============================================================================

print("\n🔹 SECTION 14: NAMING CONVENTIONS")
print("-" * 50)

print("""
PYTHON NAMING CONVENTIONS:

1. snake_case: Variables and functions
   Example: user_name, total_price, calculate_tax()

2. PascalCase/CapWords: Classes
   Example: BankAccount, DataScienceModel

3. UPPER_CASE: Constants
   Example: PI, MAX_SPEED, DEFAULT_TIMEOUT

4. _single_underscore: Private variables (by convention)
   Example: _password, _config

5. __double_underscore: Name mangling
   Example: __secret_key

6. __dunder__: Special methods
   Example: __init__, __str__, __len__
""")

# Examples of each convention
total_cost = 100.50          # snake_case for variables
PI = 3.14159                 # UPPER_CASE for constants
_internal_config = "secret"  # _single for private

class BankAccount:           # PascalCase for classes
    def __init__(self, balance):  # __dunder__ for special methods
        self.balance = balance
        self._account_number = "123456"  # _single for private

# ============================================================================
# SECTION 15: MULTIPLE VARIABLE ASSIGNMENT
# ============================================================================

print("\n🔹 SECTION 15: MULTIPLE VARIABLE ASSIGNMENT")
print("-" * 50)

print("You can assign multiple variables in one line:")

# Multiple assignment
x, y, z = 1, 2.5, "Python"
print(f"x, y, z = 1, 2.5, 'Python'")
print(f"x = {x} (type: {type(x).__name__})")
print(f"y = {y} (type: {type(y).__name__})")
print(f"z = '{z}' (type: {type(z).__name__})")

# Assign same value to multiple variables
a = b = c = 10
print(f"\na = b = c = 10")
print(f"a = {a}, b = {b}, c = {c}")

# ============================================================================
# SECTION 16: DELETING VARIABLES
# ============================================================================

print("\n🔹 SECTION 16: DELETING VARIABLES")
print("-" * 50)

print("You can delete variables using the 'del' keyword:")

# Create a variable
temp_var = "I will be deleted"
print(f"temp_var = '{temp_var}'")

# Delete the variable
del temp_var
print("del temp_var  # Variable deleted from memory")

print("# print(temp_var)  # This would cause NameError now")

# ============================================================================
# SECTION 17: PRACTICAL EXAMPLES
# ============================================================================

print("\n🔹 SECTION 17: PRACTICAL EXAMPLES")
print("-" * 50)

print("Let's put it all together with practical examples:")

# Example 1: Calculator
print("\n📝 EXAMPLE 1: Simple Calculator")
num1 = 15
num2 = 4

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")

# Example 2: Grade checker
print("\n📝 EXAMPLE 2: Grade Checker")
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}")
print(f"Grade: {grade}")

# Example 3: Shopping cart
print("\n📝 EXAMPLE 3: Shopping Cart")
item_price = 25.99
quantity = 3
tax_rate = 0.08

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Item price: ${item_price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax ({tax_rate*100}%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

print("\n" + "=" * 60)
print("END OF COMPREHENSIVE GUIDE")
print("=" * 60)
