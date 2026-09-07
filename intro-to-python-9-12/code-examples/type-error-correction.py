"""Public portfolio example for Lesson 1.3: Reading Errors as Information.

Verified with Python 3.12.
"""

age = 16

# Broken version from the lesson:
# print("I am " + age)
# TypeError: can only concatenate str (not "int") to str

# Corrected version:
print("I am", age)
