import os

def main():
    # Local variables
    name = ''
    golf_score = 0
    num_players = 0

    # Prompt user for the number of players
    name_search = input("Enter the name of the player to remove: ")

    # Open golf.txt for reading
    infile = open('golf1.txt', 'rt')

    #Open temp.txt for writing/updating
    temp_working_file = open('temp.txt','wt')

    print("Name of the file: ", infile.name)
    print("Is the file closed? ", infile.closed)
    print("File is open in what mode? ", infile.mode)
    print("Where is the cursor? ", infile.tell())
    change_cursor_location = infile.seek(0,0)

    name = infile.readline()
    #name = infile.readlines(10) reads 10 lines
    while name != '':
        score = infile.readline()
        name = name.rstrip("\n")

        # Write data to file
        if name != name_search:
            temp_working_file.write(name + '\n')
            temp_working_file.write(str(score) + '\n')
            print("Where is the cursor? ", infile.tell())
                    
        # Continue reading the file, move to next line
        name = infile.readline()

    infile.close()
    temp_working_file.close()

    os.remove('golf1.txt') #remove a file
    os.rename('temp.txt', 'golf1.txt') #rename a file
    #os.mkdir('/tmp') make directory
    #os.rmdir('/tmp') remove directory
    #os.chdir('/tmp') change directory
    #os.getcwd() get current working directory
    
# Call the main function.
main()
