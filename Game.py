#Name: Hadi Abdelaal. 

#Function to display instructions.
def show_instructions():
    # print a main menu and the commands
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'\n")


# The main function
def main():
    # Calling function to display instructions
    show_instructions()
    # A dictionary linking a room to other rooms
    # And linking one item for each room
    rooms = {'Great Hall': {'South': 'Bedroom', 'North': 'Dungeon', 'East': 'Kitchen', 'West': 'Library', 'item': None},
             'Bedroom': {'North': 'Great Hall', 'East': 'Cellar', 'item': 'Armor'},
             'Cellar': {'West': 'Bedroom', 'item': 'Helmet'},
             'Dining Room': {'South': 'Kitchen', 'item': 'Dragon'},
             'Dungeon': {'East': 'Gallery', 'South': 'Great Hall', 'item': 'Sword'},
             'Library': {'East': 'Great Hall', 'item': 'Book'},
             'Gallery': {'West': 'Dungeon', 'item': 'Shield'},
             'Kitchen': {'West': 'Great Hall', 'North': 'Dining Room', 'item': 'Sword'}
             }

    # Starting room
    current_room = 'Great Hall'
    # List to store collected items
    inventory = []

    # Loop to simulate moves between rooms based on the user input
    while True:
        # If the current_room is Dining Room then breaking the loop
        if current_room == 'Dining Room':
            print("\nYou are in the", current_room)
            print("You see a Dragon!", )
            if len(inventory) == 6:
                print("\nCongratulations! You have collected all items and defeated the dragon!")
            else:
                print("\nNOM NOM...GAME OVER!")
            break

        # Printing the current_room
        print("\nYou are in the", current_room)

        # Taking the user opinion to pick the item or not
        if rooms[current_room]['item'] != None:
            print("You see a", rooms[current_room]['item'])
            opinion = input("get " + rooms[current_room]['item'] + "?(Y/N): ").upper()
            # Validating the user input
            while opinion not in ['Y', 'N']:
                print("Invalid input. Try again")
                opinion = input("Get " + rooms[current_room]['item'] + "?(Y/N): ").upper()
            if opinion == 'Y':
                inventory.append(rooms[current_room]['item'])
                rooms[current_room]['item'] = None
        else:
            print("Already item collected or nothing in this room")

        # Printing the inventory
        print("Inventory:", inventory)

        # Taking user input for direction to move
        direction = input("Direction to move?(East,West,North,South): ").title()
        directions = list(rooms[current_room].keys())
        directions.remove('item')
        # Validating the direction
        while direction not in directions:
            print("Invalid direction from " + current_room + ". Try again")
            direction = input("Direction to move?(East,West,North,South): ").title()

        # Setting the next_room
        next_room = rooms[current_room][direction]
        print("You have just moved to", next_room)
        print("------------------------------------------------")

        # Updating the current_room
        current_room = next_room

    # Printing the end message
    print("\nThanks for playing the game. Hope you enjoyed it.")


# Calling the main function
main()
