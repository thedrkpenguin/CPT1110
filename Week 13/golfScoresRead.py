def main():
    # Local variables
    line = ''
    name = ''
    golf_score = 0
    num_players = 0

    # Open golf.txt for reading
    infile = open('golf.txt', 'r')

    # Read first name
    name = infile.readline() #reads one line at a time
    #file_content = infile.read() #reads entire contents
    
    # Read until no data 
    while name != '':
        # Read score
        golf_score = int(infile.readline())
        
        
        # Strip '\n'
        name = name.rstrip('\n')

        # Display data with one line space between the data 
        # for every two players 
        print('Name:', name)
        print('Golf Score:', golf_score)
        
        # Read next name
        name = infile.readline()

    # Close file
    infile.close()

# Call the main function.
main()
