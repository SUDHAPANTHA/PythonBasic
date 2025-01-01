import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
# value = roll()
# print(value) print random value 
while True:
    players = input("Enter the number of players(1 - 4): ")
    if players.isdigit():
        players=int(players) #convertung the string into number
        if 2 <= players <= 4:
            print("Must be between 2 - 4 players.")
            break
    else:
        print("Invalid, try again.")
print (players)