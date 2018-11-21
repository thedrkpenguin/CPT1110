infile = open('golf.txt', 'r')
contents = infile.read()
print(contents)
infile.close()



with open('golf.txt','r') as infile:
    contents = infile.read()
    print(contents) #.close() is called automatically

