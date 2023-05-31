# ^Fran -> all strings that start with 'Fran'
# Fran$ -> all strings that start with 'Fran'
# \d match a single numerical digit [0-9]
# \d\d match a double digit [0-9]
#\s match a single whitespace character
#\w matches a-z, A-Z, 0-9, _
# ^ \w\w\w\w\s -> matches 4 consecutive word character and a whitespace character
# * -> 0+
# + -> 1+ (positive number of occurrences)
# ? -> 0 or 1
# {n} Exactly n occurrences

import re

# Pattern for only uppercase characters
# pattern = re.compile("^[A-Z]+$")
# print(pattern.search("Hello"))
# print(pattern.search(" HELLO "))
# print(pattern.search(" HELLO"))
# print(pattern.search(""))
# print(pattern.search("H"))

# Pattern for only lowercase characters
# pattern = re.compile("^[a-z]+$")
# print(pattern.search("Hello"))
# print(pattern.search(" HELLO "))
# print(pattern.search(" HELLO"))
# print(pattern.search(""))
# print(pattern.search("H"))

# Pattern for only mixed case characters
pattern = re.compile("^[a-zA-Z\d\s]+$")
print(pattern.search("Hello"))
print(pattern.search(" HEL4LO "))
print(pattern.search(" HELLO"))
print(pattern.search(""))
print(pattern.search("H"))

# Pattern for 3 lowercase letters, 3-5 digits, one symbol, and two optional uppercase letters
# pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
# print(pattern.search("lll1234&AA"))
# print(pattern.search("lll1234&"))

# pattern for length of 10 for any characters 
# pattern = re.compile("^.{10}$")
# print(pattern.search("lll1234&AA"))
# print(pattern.search("lll1234&"))

#pattern for email addresses
# pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,}$")
