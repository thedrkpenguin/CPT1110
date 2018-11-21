import re  #import regular expressions module/library
import time # import time module/library

#Download mbox.txt file from http://www.py4inf.com/code/mbox.txt
#mboxFile = open('c:/users/burkholder.p/downloads/tmp/mbox.txt','r')
mboxFile = open('mbox.txt','r')

count = 0

for line in mboxFile:
    count += 1
print("The number of lines in the file mbox.txt is", count)
print("Sleeping 5 seconds....")
time.sleep(5)

mboxFile.seek(0)  #resets pointer to beginning of the file

count = 0
for line in mboxFile:
    line = line.rstrip()
    if line.find('From') == -1:  #case sensitive
        continue
    print(line)
    count += 1  #(3599)
    
print("The total number of lines containing the word 'From' is ", count)
print("Sleeping 5 seconds....")
time.sleep(5)

mboxFile.seek(0)  #resets pointer to beginning of the file

count = 0
for line in mboxFile:
    line = line.rstrip()
    if line.startswith('From'):  #case sensitive
        print(line)
        count += 1 #(3594)
    
print("The total number of lines that starts with the word 'From' is ", count)

mboxFile.close()
