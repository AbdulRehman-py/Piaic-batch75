my_string: str = 'Hello! World'

# split into a list of words
words: list[str] = my_string.split()  # Fixed: should be list[str], not str
print("my_string.split()    = ", words)

# words = my_string.split(" ") # Space as a delimiter
# print('my_string.split(" ") = ',words)

# words = my_string.split("l") # Splitting using 'l' as the delimiter
# print('my_string.split("l") = ', words)

# ============================================================================
# STRING SPLIT() METHOD - DETAILED EXPLANATION
# ============================================================================

print("\n" + "="*60)
print("STRING SPLIT() METHOD EXPLAINED")
print("="*60)

print("""
WHAT IS split()?
- split() is a string method that breaks a string into a list
- It divides the string at specified separators (delimiters)
- Returns a list of substrings
- Very useful for processing text data
""")

# ============================================================================
# BASIC EXAMPLES
# ============================================================================

print("\n🔹 BASIC EXAMPLES:")
print("-" * 40)

# Example 1: Default splitting (whitespace)
text1 = "Hello World Python"
result1 = text1.split()
print(f"'{text1}'.split() = {result1}")
print(f"Type: {type(result1)}")

# Example 2: Splitting with spaces
text2 = "apple banana orange"
result2 = text2.split(" ")
print(f"'{text2}'.split(' ') = {result2}")

# Example 3: Multiple spaces (default split handles this)
text3 = "hello    world    python"  # Multiple spaces
result3a = text3.split()      # Default: handles multiple spaces
result3b = text3.split(" ")   # Explicit space: creates empty strings
print(f"'{text3}'.split() = {result3a}")
print(f"'{text3}'.split(' ') = {result3b}")

# ============================================================================
# DIFFERENT DELIMITERS
# ============================================================================

print("\n🔹 DIFFERENT DELIMITERS:")
print("-" * 40)

# Comma delimiter
csv_data = "apple,banana,orange,grape"
fruits = csv_data.split(",")
print(f"CSV: '{csv_data}'.split(',') = {fruits}")

# Pipe delimiter
pipe_data = "name|age|city|country"
fields = pipe_data.split("|")
print(f"Pipe: '{pipe_data}'.split('|') = {fields}")

# Hyphen delimiter
date_string = "2025-07-13"
date_parts = date_string.split("-")
print(f"Date: '{date_string}'.split('-') = {date_parts}")

# Custom delimiter
path = "home/user/documents/file.txt"
path_parts = path.split("/")
print(f"Path: '{path}'.split('/') = {path_parts}")

# ============================================================================
# SPLIT WITH MAXSPLIT PARAMETER
# ============================================================================

print("\n🔹 MAXSPLIT PARAMETER:")
print("-" * 40)

sentence = "The quick brown fox jumps"

# Split all
all_words = sentence.split()
print(f"All splits: {all_words}")

# Split only first 2
first_two = sentence.split(" ", 2)  # maxsplit=2
print(f"First 2 splits: {first_two}")

# Split only first 1
first_one = sentence.split(" ", 1)  # maxsplit=1
print(f"First 1 split: {first_one}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n🔹 PRACTICAL EXAMPLES:")
print("-" * 40)

# Example 1: Processing names
full_name = "Abdul Rahman Khan"
name_parts = full_name.split()
if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[-1]  # Last element
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")

# Example 2: Email processing
email = "user@example.com"
email_parts = email.split("@")
if len(email_parts) == 2:
    username = email_parts[0]
    domain = email_parts[1]
    print(f"Username: {username}")
    print(f"Domain: {domain}")

# Example 3: File extension
filename = "document.pdf"
file_parts = filename.split(".")
if len(file_parts) >= 2:
    name = file_parts[0]
    extension = file_parts[1]
    print(f"File name: {name}")
    print(f"Extension: {extension}")

# Example 4: Processing CSV-like data
student_data = "John,25,Computer Science,A"
student_info = student_data.split(",")
print(f"Student: {student_info[0]}")
print(f"Age: {student_info[1]}")
print(f"Major: {student_info[2]}")
print(f"Grade: {student_info[3]}")

# ============================================================================
# EDGE CASES AND GOTCHAS
# ============================================================================

print("\n🔹 EDGE CASES:")
print("-" * 40)

# Empty string
empty = ""
empty_split = empty.split()
print(f"Empty string split: '{empty}'.split() = {empty_split}")

# String with only delimiters
only_spaces = "   "
spaces_split = only_spaces.split()
print(f"Only spaces: '{only_spaces}'.split() = {spaces_split}")

# String with no delimiters
no_delimiter = "hello"
no_delim_split = no_delimiter.split(",")
print(f"No delimiter found: '{no_delimiter}'.split(',') = {no_delim_split}")

# Leading/trailing spaces
padded = "  hello world  "
padded_split = padded.split()
print(f"Padded string: '{padded}'.split() = {padded_split}")

# ============================================================================
# COMPARISON WITH OTHER METHODS
# ============================================================================

print("\n🔹 COMPARISON WITH OTHER STRING METHODS:")
print("-" * 40)

text = "apple,banana,orange"

# split() vs partition()
split_result = text.split(",", 1)  # Split once
partition_result = text.partition(",")  # Always returns 3 elements
print(f"split(',', 1): {split_result}")
print(f"partition(','): {partition_result}")

# split() vs rsplit() (right split)
text_r = "a.b.c.d"
left_split = text_r.split(".", 1)   # Split from left
right_split = text_r.rsplit(".", 1)  # Split from right
print(f"Left split: {left_split}")
print(f"Right split: {right_split}")

# ============================================================================
# REAL-WORLD USE CASES
# ============================================================================

print("\n🔹 REAL-WORLD USE CASES:")
print("-" * 40)

# 1. Processing log files
log_entry = "2025-07-13 10:30:45 ERROR Database connection failed"
log_parts = log_entry.split(" ", 3)  # Split into 4 parts max
date = log_parts[0]
time = log_parts[1]
level = log_parts[2]
message = log_parts[3]
print(f"Log - Date: {date}, Time: {time}, Level: {level}")
print(f"Message: {message}")

# 2. URL processing
url = "https://www.example.com/path/to/page"
url_parts = url.split("/")
protocol = url_parts[0][:-1]  # Remove the ':'
domain = url_parts[2]
print(f"Protocol: {protocol}")
print(f"Domain: {domain}")

# 3. Command line arguments simulation
command = "python script.py --input file.txt --output result.txt"
cmd_parts = command.split()
script_name = cmd_parts[1]
print(f"Script: {script_name}")
print(f"Arguments: {cmd_parts[2:]}")

print("\n" + "="*60)
print("SPLIT() METHOD SUMMARY")
print("="*60)
print("""
✅ SYNTAX: string.split(separator, maxsplit)
✅ PARAMETERS:
   - separator (optional): What to split on (default: any whitespace)
   - maxsplit (optional): Maximum number of splits (default: -1, all)

✅ RETURNS: List of strings

✅ COMMON USE CASES:
   - Processing CSV data
   - Parsing file paths
   - Splitting names
   - Processing URLs
   - Command line parsing
   - Log file analysis

⚠️  REMEMBER:
   - Always returns a list, even if no splits occur
   - Default split removes leading/trailing whitespace
   - Empty strings can appear in results with explicit delimiters
""")