#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
Hogwarts RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
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
        monster = rooms[currentRoom]["monster"]
        print(f"\nYou have come face to face with a {monster}!")
        if monster == 'dragon':
            print("""
The magnificent dragon flaps its wings and blows fire in your direction.
You narrowly jump out of the way of the burning flames.
You must act quickly if you wish to survive!
            """)
        if monster == 'basilisk':
            print("""
The gigantic basilisk, slithers across the room and opens its mouth with a hiss.
You slide under a desk, barely avoiding the deadly bite of the serpent.
You must act quickly if you wish to survive!
            """)
    # print all directions and rooms
    print("\nCurrent paths:")
    for path in rooms[currentRoom]:
        # ignore items, monsters, and hidden doors
        if path != "item" and path != "monster" and path != "hidden-door":
            print(f"{path}: {rooms[currentRoom][path]}")
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Main Hall': {
        'north': 'Entrance Hall',
        'west': 'Lessons Hallway',
        'east': 'Moving Staircases',
        'upstairs': 'Main Hall Balcony',
        'item': 'wand'
    },
    'Lessons Hallway': {
        'north': 'Charms Hallway',
        'south': 'Divination Courtyard',
        'east': 'Main Hall',
        'southeast': 'Potions Class'
    },
    # For now, the directions of the rooms don't change, but it would be cool to find a way to make it so the stairs
    # move like in the books to change which rooms they go to.
    'Moving Staircases': {
        'west': 'Main Hall',
        'east': 'House Hallway',
        'south': 'Headmaster\'s Office'
    },
    'Entrance Hall': {
        'north': 'Great Hall',
        'northeast': 'Bathroom Hallway',
        'south': 'Main Hall',
    },
    'Main Hall Balcony': {
        'downstairs': 'Main Hall',
        'west': 'Library',
        'east': 'Outer Corridor'
    },
    'Charms Hallway': {
        'northwest': 'Charms Class',
        'south': 'Lessons Hallway',
        'west': 'Charms Class 2'
    },
    'Charms Class': {
        'east': 'Charms Hallway',
        'hidden-door': 'Dragon Basement'
    },
    'Dragon Basement': {
        # Determine what to do in this room, user current gets trapped
        'monster': 'dragon'
    },
    'Charms Class 2': {
        'east': 'Charms Hallway',
        'hidden-door': 'Dark Basement'
    },
    'Dark Basement': {
        # Determine what to do in this room, user current gets trapped
    },
    'Divination Courtyard': {
        'north': 'Lessons Hallway',
        'south': 'Divination Class',
    },
    'Divination Class': {
        'north': 'Divination Courtyard'
    },
    'Potions Class': {
        'east': 'Lessons Hallway',
        'southwest': 'Potions Dungeon'
    },
    'Potions Dungeon': {
        'northeast': 'Potions Class'
    },
    'House Hallway': {
        'downstairs': 'Slytherin CR',
        'north': 'Ravenclaw Tower',
        'east': 'Moving Staircases',
        'south': 'Hufflepuff Hallway',
        'west': 'Gryffindor CR',
    },
    'Headmaster\'s Office': {
        # Continue building
    },
    'Slytherin CR': {
        'upstairs': 'House Hallway',
        'east': 'Slytherin Dorm'
    },
    'Slytherin Dorm': {
        'west': 'Slytherin CR',
        'monster': 'basilisk'
    },
    'Ravenclaw Tower': {
        'south': 'House Hallway',
        'upstairs': 'Ravenclaw CR'
    },
    'Ravenclaw CR': {
        'north': 'Ravenclaw Dorm',
        'downstairs': 'Ravenclaw Tower'
    },
    'Ravenclaw Dorm': {
        'south': 'Ravenclaw CR'
    },
    'Hufflepuff Hallway': {
        'north': 'House Hallway',
        'south': 'Hufflepuff CR'
    },
    'Hufflepuff CR': {
        'north': 'Hufflepuff Hallway',
        'south': 'Hufflepuff Dorm'
    },
    'Gryffindor CR': {
        'east': 'House Hallway',
        'west': 'Gryffindor Dorm'
    },
    'Great Hall': {
        'south': 'Entrance Hall'
    },
    'Bathroom Hallway': {
        'south': 'Entrance Hall',
        'southeast': 'Boys\' Bathroom'
    },
    'Boys\' Bathroom': {
        'north': 'Bathroom Hallway'
    },
    'Library': {
        'west': 'Restricted Section',
        'east': 'Main Hall Balcony'
    },
    'Outer Corridor': {
        'south': 'Fountain Courtyard',
        'east': 'Clock Tower Courtyard',
        'west': 'Main Hall Balcony'
    },
    'Restricted Section': {
        # Key will be needed from Headmaster's Office in order to enter
        # Add a cool item that will be very useful later
        'east': 'Library'
    },
    'Fountain Courtyard': {
        'north': 'Outer Corridor',
        'south': 'Wooden Bridge'
    },
    'Clock Tower Courtyard': {
        # Continue building
        'northeast': 'Grassy Courtyard',
        'northwest': 'Clock Tower',
        'east': 'Herbology Grounds',
        'west': 'Outer Corridor',
    },
    'Wooden Bridge': {
        'north': 'Fountain Courtyard',
        'South': 'Hogwarts Grounds'
    },
    'Hogwarts Grounds': {
        'south': 'Black Lake',
        'southwest': 'Hagrid\'s Garden',
        'west': 'Quidditch Grounds'
    },
    'Black Lake': {
        'north': 'Hogwarts Grounds'
    },
    'Hagrid\'s Garden': {
        'northeast': 'Hogwarts Garden'
    },
    'Quidditch Grounds': {
        'east': 'Hogwarts Grounds',
        'item': 'broom'
    },
    'Grassy Courtyard': {
        'north': 'Owlrey',
        'south': 'Clock Tower Courtyard'
    },
    'Clock Tower': {
        'south': 'Clock Tower Courtyard'
    },
    'Herbology Grounds': {
        'north': 'Greenhouse',
        'east': 'Training Grounds',
        'west': 'Clock Tower Courtyard'
    },
    'Greenhouse': {
        'north': 'Garden Path',
        'south': 'Herbology Grounds'
    },
    'Training Grounds': {
        'west': 'Herbology Grounds'
    },
    'Garden Path': {
        'north': 'Greenhouse 2',
        'east': 'Garden Shed',
        'south': 'Greenhouse'
    },
    'Greenhouse 2': {
        'south': 'Garden Path'
    }

}

# start the player in the Hall
currentRoom = 'Main Hall'

showInstructions()

# loop forever
while True:

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

    # if they type 'go' first
    if move[0] == 'go':
        # Check if player is attempting to enter dorm room - if so, prompt with riddle
        if len(currentRoom.split(" ")) > 1 and currentRoom.split(" ")[1] == "CR" and rooms[currentRoom][move[1]].split(" ")[1] == "Dorm":
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

        # check that they are allowed wherever they want to go
        elif move[1] in rooms[currentRoom]:
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
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')


