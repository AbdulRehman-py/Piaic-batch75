# PYTHON OPERATORS & VARIABLES - QUICK REFERENCE GUIDE
# ========================================================

"""
This is a quick reference guide for all Python operators and variables.
For detailed explanations with examples, see operators.py
"""

# ============================================================================
# OPERATORS QUICK REFERENCE
# ============================================================================

"""
1. ARITHMETIC OPERATORS:
   +    Addition           (5 + 3 = 8)
   -    Subtraction        (5 - 3 = 2)
   *    Multiplication     (5 * 3 = 15)
   /    Division (float)   (5 / 3 = 1.667)
   //   Floor Division     (5 // 3 = 1)
   %    Modulus           (5 % 3 = 2)
   **   Exponentiation    (5 ** 3 = 125)

2. COMPARISON OPERATORS:
   ==   Equal to           (5 == 5 → True)
   !=   Not equal to       (5 != 3 → True)
   >    Greater than       (5 > 3 → True)
   <    Less than          (5 < 3 → False)
   >=   Greater or equal   (5 >= 5 → True)
   <=   Less or equal      (5 <= 3 → False)

3. LOGICAL OPERATORS:
   and  Both True          (True and True → True)
   or   At least one True  (True or False → True)
   not  Opposite           (not True → False)

4. ASSIGNMENT OPERATORS:
   =    Basic assignment   (x = 5)
   +=   Add and assign     (x += 3 → x = x + 3)
   -=   Subtract and assign (x -= 3 → x = x - 3)
   *=   Multiply and assign (x *= 3 → x = x * 3)
   /=   Divide and assign  (x /= 3 → x = x / 3)
   //=  Floor div and assign (x //= 3 → x = x // 3)
   :=   Walrus operator    (if (n := len(data)) > 5:)

5. IDENTITY OPERATORS:
   is      Same object     (a is b)
   is not  Different object (a is not b)

6. MEMBERSHIP OPERATORS:
   in      Value exists    (3 in [1,2,3] → True)
   not in  Value missing   (5 not in [1,2,3] → True)

7. UNARY OPERATORS:
   -    Negative           (-5)
   not  Logical NOT        (not True → False)
   ~    Bitwise NOT        (~5 = -6)
"""

# ============================================================================
# VARIABLES QUICK REFERENCE
# ============================================================================

"""
VARIABLE NAMING RULES:
1. Can contain letters, digits, underscores (_)
2. Cannot start with digit
3. Case-sensitive
4. Cannot use keywords
5. No spaces or special chars (except _)

NAMING CONVENTIONS:
- snake_case: variables, functions (user_name, calculate_tax)
- PascalCase: classes (BankAccount, User)
- UPPER_CASE: constants (PI, MAX_SIZE)
- _private: internal use (_config)
- __mangled: avoid external access (__secret)
- __dunder__: special methods (__init__)

ASSIGNMENT EXAMPLES:
- Single: x = 5
- Multiple: x, y, z = 1, 2, 3
- Same value: a = b = c = 10
- Type hints: age: int = 25

DELETE VARIABLES:
- del variable_name
"""

# ============================================================================
# COMMON PATTERNS & EXAMPLES
# ============================================================================

def common_patterns():
    """Common usage patterns for operators and variables"""
    
    # Chained comparisons
    age = 25
    if 18 <= age <= 65:
        print("Working age")
    
    # Walrus operator
    if (n := len("hello")) > 3:
        print(f"String length is {n}")
    
    # Multiple assignment
    x, y = 10, 20
    
    # Swapping variables
    x, y = y, x
    
    # Membership testing
    fruits = ["apple", "banana", "orange"]
    if "apple" in fruits:
        print("Apple found")
    
    # Identity vs equality
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"a == b: {a == b}")  # True (same values)
    print(f"a is b: {a is b}")  # False (different objects)
    print(f"a is c: {a is c}")  # True (same object)

# ============================================================================
# OPERATOR PRECEDENCE (HIGHEST TO LOWEST)
# ============================================================================

"""
OPERATOR PRECEDENCE:
1. ()           Parentheses
2. **           Exponentiation
3. +x, -x, ~x   Unary plus, minus, bitwise NOT
4. *, /, //, %  Multiplication, division, floor division, modulus
5. +, -         Addition, subtraction
6. <<, >>       Bitwise shifts
7. &            Bitwise AND
8. ^            Bitwise XOR
9. |            Bitwise OR
10. ==, !=, <, <=, >, >=, is, is not, in, not in  Comparisons
11. not         Boolean NOT
12. and         Boolean AND
13. or          Boolean OR
14. :=          Walrus operator
"""

# ============================================================================
# PYTHON KEYWORDS (CANNOT BE USED AS VARIABLE NAMES)
# ============================================================================

"""
PYTHON KEYWORDS (35 total):
False, None, True, and, as, assert, async, await, break, class, 
continue, def, del, elif, else, except, finally, for, from, 
global, if, import, in, is, lambda, nonlocal, not, or, pass, 
raise, return, try, while, with, yield
"""

if __name__ == "__main__":
    print("Quick Reference Guide for Python Operators & Variables")
    print("For detailed examples, run: python operators.py")
    common_patterns()
