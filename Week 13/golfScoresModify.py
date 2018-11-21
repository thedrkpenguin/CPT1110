import os

def main():
    # Local variables
    name = ''
    golf_score = 0
    num_players = 0

    # Prompt user for the number of players
    name_search = input("Enter the name of the player to modify: ")
    new_score = int(input("Enter their new score: "))

    # Open golf.txt for reading
    infile = open('golf1.txt', 'r')

    #Open temp.txt for writing/updating
    temp_working_file = open('temp.txt','w')

    name = infile.readline()
    while name != '':
        score = infile.readline()
        name = name.rstrip("\n")

        # Write data to file
        if name == name_search:
            temp_working_file.write(name + '\n')
            temp_working_file.write(str(new_score) + '\n')
        else:
            temp_working_file.write(name + '\n')
            temp_working_file.write(str(score) + '\n')
            
        # Continue reading the file, move to next line
        name = infile.readline()

    infile.close()
    temp_working_file.close()

    os.remove('golf1.txt')
    os.rename('temp.txt', 'golf1.txt')
    
# Call the main function.
main()
