#!/usr/bin/python3

from monsters import dragon, basilisk, dementors
from rooms import hogwarts_rooms
from player import player_class
from intro_story import story


# an inventory, which is initially empty
inventory = []


# all monsters must be defeated to win. This is a tracker of the live monsters, once the list is empty, the player wins.
monsters = ['dragon', 'basilisk', 'dementors']

# Large dictionary with all of the connected rooms imported
rooms = hogwarts_rooms.rooms

# start the player in the Main Hall
currentRoom = 'Main Hall'

# Create a new player - prompts player to enter name
player = player_class.new_player(inventory)

# Check to see if player lost to monster
monster_won = False

def showInstructions():
    # print a main menu and the commands
    print(f'''
How to play:
============
Commands:
  go [direction]
  get [item]
  q <quit game>
  i <show instructions>
    ''')

def game_kickoff():
    print(f"\nMake haste {player.name}! Hogwarts is in dire need of your help!")
    # Kick off story to player
    story.print_story()
    input("Press enter to continue!")
    showInstructions()
    input("Press enter to begin your quest!")


def showStatus():
    inventory = player.inventory
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print current health
    print('Health : ' + str(player.health))
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('\nYou see a ' + rooms[currentRoom]['item'])
    # hint at hidden door if there is one
    if "hidden-door" in rooms[currentRoom]:
        print('\nSomething feels off about this room, almost as if there is a hidden-door...')
        # if room contains a monster
    if "monster" in rooms[currentRoom]:
        handle_monster()
        # If the monster won, break out of function
        if monster_won:
            return
    # print all directions and rooms
    print("\nCurrent paths:")
    for path in rooms[currentRoom]:
        # ignore items, monsters, and hidden doors
        if path != "item" and path != "monster" and path != "hidden-door":
            print(f"{path}: {rooms[currentRoom][path]}")
    print("---------------------------")


# Kick off monster storyline scenarios
def handle_monster():
    global monster_won
    inventory = player.inventory
    monster = rooms[currentRoom]["monster"]

    if monster != 'dementors':
        print(f"\nYou have come face to face with a {monster}!")

    if monster == 'dragon':
        # Will return true or false if monster was defeated. If not, the game was lost
        if dragon.dragon_encountered(inventory, player):
            monster_defeated('dragon')
            rooms[currentRoom]['narrow-path'] = 'Charms Class'
        else:
            monster_won = True
    elif monster == 'basilisk':
        # Will return true or false if monster was defeated. If not, the game was lost
        if basilisk.basilisk_encountered(inventory, player):
            monster_defeated('basilisk')
            rooms[currentRoom]['west'] = 'Slytherin CR'
        else:
            monster_won = True
    elif monster == 'dementors':
        # Will return true or false if monster was defeated. If not, the game was lost
        if dementors.dementors_encountered(inventory, player):
            monster_defeated('dementors')
            rooms[currentRoom]['west'] = 'Herbology Grounds'
        else:
            monster_won = True


# Monster has been defeated, remove from monsters list and remove from room
def monster_defeated(remove_monster):
    del rooms[currentRoom]['monster']
    monsters.remove(remove_monster)

# Allow or deny access to Restricted Section
def restricted_access():
    global currentRoom
    if 'key' in inventory:
        currentRoom = rooms[currentRoom][move[1]]
        player.inventory.remove('key')
        print('You reach for the key as you enter, but the key has vanished.')
    else:
        print('Access to the Restricted Section is reserved to those with permission from the Headmaster.')

# Allow or deny access to Headmaster's Office
def office_access():
    global currentRoom
    print("""
What's the password?
Enter "A" for Quidditch
"B" for Sherbet Lemon
"C" for Hocus Pocus
"D" for Gillyweed
    """)

    print('---------------------------')
    answer = input(">").strip().upper()

    if answer == "B":
        # Only add key if this is the first entry and player does not already hold key
        # Player will also have access to key if needed after using it in the restricted section
        if 'key' not in inventory and 'item' not in rooms['Headmaster\'s Office']:
            rooms['Headmaster\'s Office']['item'] = 'key'
        currentRoom = rooms[currentRoom][move[1]]
    else:
        print("\nThat is incorrect.")

# Allow or deny access to dorm room
def dorm_access():
    global currentRoom
    # For now, for simplicity, every room will have the same riddle, but in future can have random
    # riddles or specific ones to each house
    print("""
In order to enter the house dorm, you must first answer this riddle. 
Answer correctly and you may enter. 
Answer incorrectly and face the consequences.
    """)
    print('''
            I'm often very stern,
            I wear my hair up in a bun,
            I'm really very fair,
            I find Quidditch very fun.
            Who am I?

Enter "A" for Albus Dumbledore - 
"B" for Harry Potter - 
"C" for Hermione Granger - 
"D" for Minerva McGonagall
    ''')

    print('---------------------------')
    answer = input(">").strip().upper()

    # If answered correctly, they continue to the respective Dorm
    if answer == "D":
        currentRoom = rooms[currentRoom][move[1]]
    # Otherwise they are taken to Headmaster's Office
    else:
        print("""
You have been caught by Professor Minerva McGonagall for trying to sneak into another houses dorm!
She takes you directly to the Headmaster's Office!
        """)
    currentRoom = "Headmaster\'s Office"




# Kick of game, followed by while loop
# showInstructions()
game_kickoff()

# loop forever
while True:

    if player.health <= 0:
        print(f"""
Your health has declined to {player.health}, which means your heart is no longer beating.

GAME OVER
        """)
        break
    elif monster_won:
        break

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # Allow player to quit
    if move[0] == 'q':
        break
    elif move[0] == 'i':
        showInstructions()

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # If player attempts to enter Restricted Section, they must have the key
            if currentRoom == 'Library' and rooms[currentRoom][move[1]] == 'Restricted Section':
                restricted_access()
            # If player attempts to enter Headmaster's Office from stairs, they need the password
            elif currentRoom == 'Moving Staircases' and rooms[currentRoom][move[1]] == 'Headmaster\'s Office':
                office_access()
            # Check if player is attempting to enter dorm room - if so, prompt with riddle
            elif len(currentRoom.split(" ")) > 1 and currentRoom.split(" ")[1] == "CR" and rooms[currentRoom][move[1]].split(" ")[1] == "Dorm":
                dorm_access()
            else:
                # set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]

        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            player.inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')





