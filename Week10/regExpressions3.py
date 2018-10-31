import re  #import regular expressions module/library
import time # import time module/library

#Download mbox.txt file from http://www.py4inf.com/code/mbox.txt
mboxFile = open('c:/users/burkholder.p/downloads/tmp/mbox.txt','r')

count = 0

for line in mboxFile:
    if re.search('from', line): #looks for first match anywhere in the string,
                                #.findall looks for all matches in the string
        print(line)
        count += 1 #(16328)
        
print("The number of lines is", count)
print("Sleeping 5 seconds....")
time.sleep(5)

mboxFile.seek(0)  #resets pointer to beginning of the file

count = 0

for line in mboxFile:
    if re.match('from', line):  #looks for match at beginning of the string
        print(line)
        count += 1 #(0)
    
print("The total number of lines is ", count)

mboxFile.close()
