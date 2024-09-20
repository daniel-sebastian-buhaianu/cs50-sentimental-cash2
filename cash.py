# Main program
def main():
    # Get the user's input in dollars
    dollars = getUserInput()
    
    # Convert dollars to cents and round to avoid floating point issues
    cents = round(dollars * 100)
    
    # Calculate and print the minimum number of coins
    print(getCoins(cents))

# Asks user for change (in dollars) and re-prompt for valid input
def getUserInput():
    while True:
        try:
            userInput = float(input("Change owed: $"))
            if userInput > 0:
                return userInput
        except ValueError:
            # If input isn't a valid float, re-prompt
            pass

# Calculates the minimum number of coins required
def getCoins(cents):
    coins = 0
    for coin_value in [25, 10, 5, 1]:
        coins += cents // coin_value  # Get how many coins of this type
        cents %= coin_value  # Update remaining cents

    return coins

# Run the program
if __name__ == "__main__":
    main()

