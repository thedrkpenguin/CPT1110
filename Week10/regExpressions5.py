#Special Characters for Regular Expressions
# '.' - dot matches any character excpet a newline
# '^' - caret matches start of string or beinning of line
# '$' - dollar sign matches the end of a string just before the newline
# '*' - asterisk matches 0 or more repetitions of preceding expression (ab* would match a, ab, abb, abbb, etc)
# '+' - plus sign mathces 1 or more repetitions of preceding expression (ab+ would match ab, abb, abbb, NOT a)
# '?' - question mark matches 0 or 1 repetitions of the preceding expression (ab? would match a or ab)
# {m} - matches m repetitions of the preceding expression (a{6} matches aaaaaa, not aaaaa)
# {m,n} - mathecs m to n r repetitions of the preceding expression (if the string is aaaaaa, a{3,5} will match aaa)
# [] - matches a set of characters ([abc012] would match a, b, c, 0, 1, or 2. ranges can ge set by using a dash (-))
# | - pipe means OR (a|b would match either a or b)


import re  #import regular expressions module/library
import time # import time module/library

#Download mbox.txt file from http://www.py4inf.com/code/mbox.txt
mboxFile = open('mbox.txt','r')

count = 0

for line in mboxFile:
    line = line.rstrip()
    match = re.findall('[a-zA-Z][a-zA-Z]\S*@\S*[a-zA-Z]', line) #matches strings starting with the range shown, an @ symbol, and
                                                        #the range shown. The \S matches non-whitespace characters(for
                                                        #example ignores spaces). This should pull out only email
                                                        #addresses
    if len(match) > 0:
        print(match)
        count += 1 #(22009)
        
print("The number of lines is", count)
print("Sleeping 5 seconds....")
time.sleep(5)

mboxFile.seek(0)  #resets pointer to beginning of the file

count = 0

for line in mboxFile:
    line = line.rstrip()
    match = re.findall('[a-zA-Z]\S*@\Suct.ac.za', line)
    if len(match) > 0: 
        print(match)
        count += 1 #()
    
print("The total number of lines is ", count)

mboxFile.seek(0)  #resets pointer to beginning of the file

count = 0

for line in mboxFile:
    line = line.rstrip()
    
        
print("The total number of lines is ", count)

mboxFile.close()
