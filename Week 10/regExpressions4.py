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
    if re.search('^F..m', line): #matches beginning strings starting with F and ending with m, but only 4 characters long
        #print(line)
        count += 1 #(3594)
        
print("The number of lines is", count)
print("Sleeping 5 seconds....")
time.sleep(5)

mboxFile.seek(0)  #resets pointer to beginning of the file

count = 0

for line in mboxFile:
    line = line.rstrip()
    if re.search('^From:.+@', line): #matches beginning strings starting with From: followed by one or
                                     #more characters followed by an @ symbol
        #print(line)
        count += 1 #(1797)
    
print("The total number of lines is ", count)

mboxFile.seek(0)  #resets pointer to beginning of the file

count = 0

for line in mboxFile:
    line = line.rstrip()
    if re.search('^From:.+@uct.ac.za', line): #matches beinning of strings starting wiht From: followed by one or
                                              #more characters followed by an @ symbol followed by uct.ac.za
        print(line)
        count +=1 #(96)
        
print("The total number of lines is ", count)

mboxFile.close()
