# What is the minimum number of characters that need to be added to the password "aB1ef" to make it strong, according to the strongPassword function?

# Explanation: The strongPassword function checks for the following conditions:

# The password should have at least 6 characters.
# The password should have at most 20 characters.
# The password should contain at least one lowercase letter, one uppercase letter, and one digit.
# The password should not contain three repeating characters in a row.
# The function returns the minimum number of characters that need to be added to the password to make it strong.

s = input()

add = 0

if len(s) < 6:
    add = 6 - len(s)

lower = False
upper = False
digit = False

for ch in s:
    if ch.islower():
        lower = True
    elif ch.isupper():
        upper = True
    elif ch.isdigit():
        digit = True

if not lower:
    add += 1

if not upper:
    add += 1

if not digit:
    add += 1

print(add)