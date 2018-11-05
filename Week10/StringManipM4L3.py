import re

user_string = str(input("Please enter a string of text: "))
first_letter_cap = []

modified_string = re.split('([.!?] *)', user_string)
for ch in modified_string:
    ch = ch.capitalize()
    first_letter_cap.append(ch)

"""

modified_string = user_string.split(". ")
for ch in modified_string:
    ch  = ch.capitalize()
    first_letter_cap.append(ch)
"""

print("You entered: ", user_string)
print("Here is the string with sentences capitalized: ", ' '.join(first_letter_cap))
print("Here is the string in all CAPS: ", user_string.upper())
print("Here is the string in all lowercase: ", user_string.lower())
print("Here is the string in title case: ", user_string.title())
