def main():
    # Local variables
    name = ''
    golf_score = 0
    num_players = 0

    # Prompt user for the number of players
    num_players = int(input('Enter the number of ' \
                            'players in the tournament: '))

    # Open golf.txt for writing
    outfile = open('golf1.txt', 'w')
    
    # Write data to file
    for i in range(num_players):
        # Prompt for name and score
        name = input('Enter the name of the player: ')
        golf_score = int(input('Enter the golf score: '))

        # Write data to file
        outfile.write(name + '\n')
        outfile.write(str(golf_score) + '\n')

    # Close file
    outfile.close()

# Call the main function.
main()
