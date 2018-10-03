names_list = ["StudentA", "StudentB", "StudentC"] #keys list
phone_list = ['1234', '5678', '9123'] #values list


phonebook = dict(zip(names_list, phone_list)) #creats dictionary from two lists
print(phonebook)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
reverse_alphabet = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

alpha_dictionary = dict(zip(alphabet,reverse_alphabet)) #creates dictionary from two strings

print(alpha_dictionary)

"""
telephone_numbers = {'Dad':'555-1234','Mom':'555-1235'}

telephone_numbers['Uncle'] = '555-4321'
telephone_numbers['Aunt'] = '555-0123'
telephone_numbers['Dad'] = ['555-1111','555-2222']
telephone_numbers['Grandma'] = '555-1111'

dictionary_comprehension = {x:x**3 for x in range(10)} #key:value
print(dictionary_comprehension)

print(telephone_numbers)
print(telephone_numbers['Dad'])
print(telephone_numbers['Mom'])

for i in telephone_numbers: #print the keys
    print(i)

for i in telephone_numbers: #print the values associated to the keys
    print(telephone_numbers[i])

for key,value in telephone_numbers.items(): #print both keys and values
    print(key,'-->',value)

if 'Dad' in telephone_numbers:
    print("Dad is found")
"""
