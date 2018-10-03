#plain_text = 'Hello'
plain_text = str(input("enter a string to encrypt: ")).upper()

my_dictionary = {'H': '1', 'e':'2', 'l':'3', 'o':'4', ' ':' '}

encrypted_text= '' #result should be 12334

"""
for letter in plain_text:
    print(letter)

for key in my_dictionary: #print the keys
    print(key)

for value in my_dictionary.values(): #print values of the keys
    print(value)

for key in my_dictionary: #print the values of the keys
    print(my_dictionary[key])

"""

for letter in plain_text: #iterate through the string
    encrypted_text += my_dictionary[letter]
print(encrypted_text)
    

