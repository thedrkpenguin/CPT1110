def main():
    # Declare variables
    line = ''
    total = 0.0
    number = 0.0

    # Open numbers.txt file for reading
    infile = open('numbers.txt', 'r')

    for line in infile:
        number = float(line)
        total += number
        
    # Close file
    infile.close()

    # Display the total of the numbers in the file
    print('Total: ', total)

# Call the main function.
main()

