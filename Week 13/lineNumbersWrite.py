def main():
    # Declare variables
    line = ''
    counter = 0
    
    # Prompt for file name
    fileName = input('Enter the name of the file: ')

    # Open the specified file for reading
    infile = open(fileName, 'r')

    for line in infile:
        counter += 1
        print(counter, end='')
        print(':', end=' ')
        
        # Strip the '\n' from the end of the line
        line = line.rstrip('\n')
        print(line)

    # Close file
    infile.close()

# Call the main function.
main()

