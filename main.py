#!/usr/bin/python3



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
    # print current health
    print('Health : ' + str(health))
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
            if 'wand' in inventory and 'sword' in inventory:
                print("""
With your wand at the ready, you must come up with a spell to distract the dragon!
Enter "A" for Aqua Eructo to shoot a stream of water at the dragon.
"B" for Langlock to stick the dragon's tongue to the tip of its mouth.
"C" fo Flipendo to knock the dragon backwards
                """)
                print('---------------------------')
                answer = input('>').strip().upper()

                # If they select the correct spell, they are taken on a winning path against the dragon
                if answer == "A":
                    print("""
Like a firehose, water bursts from the tip of your wand, forcing the dragon towards the corner of the room.
You know that charms and jinx won't penetrate the dragon's thick skin, so you must be clever.
                    """)
                    if 'broom' in inventory:
                        print("""
You swiftly use the Accio summoning charm to call your broom, mounting it.
Flying around the dragon, you confuse it with your speed, giving you time to brandish your sword.
You fly below the belly of the dragon, thrusting your sword into the stomach of the creature.
Just as you clear the dragon above you, it stumbles to the ground, its body shaking the ground and walls.
Beyond the tail of the dragon, you can now see the exit. 
                        """)
                        del rooms[currentRoom]['monster']
                        monsters.remove('dragon')
                        rooms[currentRoom]['narrow-path'] = 'Charms Class'
                    else:
                        print("""
Three spells come to your mind:
Enter "A" for Defodio to dig and carve through the dragon.
"B" for Moblicorpus to levitate and move the dragon.
"C" for Wingardium Leviosa to levitate a large rock onto the dragon.
                        """)

                        print('---------------------------')
                        answer = input('>').strip().upper()

                        # winning spell
                        if answer == 'C':
                            print("""
You cast Wingardium Leviosa to the largest rock you can see, causing the rock smash into the dragon.
The dragon falls to the ground, shaking its head from the blunt of the rock.
With spared time, you brandish your sword, jabbing it into the side of the dragon.
It swats you away, causing you to take on 25 points of damage when you hit a wall.
Luckily for you, the sword was enough to cause the dragon to bleed out, giving you access to an exit.
                            """)
                            del rooms[currentRoom]['monster']
                            monsters.remove('dragon')
                            rooms[currentRoom]['narrow-path'] = 'Charms Class'
                            # health -= 25
                        # Other spells fail and the player loses
                        else:
                            print("""
When it is too late, you remember that your spell cannot penetrate the skin of the dragon.
The dragon breathes fire onto your hand, knocking your wand away.
You reach for your sword, but the dragon is too quick, moving its flames to your other hand.
You become overwhelmed in the fire with no other options.
\nGAME OVER
                            """)
                            return
                # Any other spell will fail, causing more effort to win against the dragon
                # This scenario is not yet completed
                else:
                    print("""
You cast a spell at the dragon, but it cannot penetrate the dragon's skin and fails to work.
Aggravated, the dragon swings its tail and knocks you to the ground. Your wand flies through the air.
********************************************************************************************************
                    """)
            # without a sword, the wizard has no means to win
            elif 'wand' in inventory:
                print("""
You raise your want, but as you are about to cast your first spell, the dragon knocks you to the ground.
Your wand snaps as you fall to the hard ground.
The dragon takes a deep breath, letting out one last burst of flames.
\nGAME OVER
                """)
                return
            # without a wand, the wizard cannot get close enough to the dragon to use the sword
            elif 'sword' in inventory:
                print("""
You jump to action, brandishing your sword. 
The dragon flaps its wings in intimidation, shaking the ground beneath you as it lands.
You take a swing at the dragons stomach, but you are too close and too slow.
The dragon opens its mouth, swiftly wrapping it around your head.
\nGAME OVER
                """)
                return
            # would you fight a dragon with nothing but your hands?
            else:
                print("""
With no defenses, you trimmer in fear, only to be engulfed by the flames of the dragon.
\nGAME OVER
                """)
                return
        elif monster == 'basilisk':
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

# player health set to 100 at start
health = 100

# all monsters must be defeated to win. This is a tracker of the live monsters, once the list is empty, the player wins.
monsters = ['dragon', 'basilisk']

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
        'north': 'Moving Staircases'
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
        'east': 'Library',
        'item': 'sword'
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
        'south': 'Hogwarts Grounds'
    },
    'Hogwarts Grounds': {
        'north': 'Wooden Bridge',
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
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # If player attempts to enter Restricted Section, they must have the key
            if currentRoom == 'Library' and rooms[currentRoom][move[1]] == 'Restricted Section':
                if 'key' in inventory:
                    currentRoom = rooms[currentRoom][move[1]]
                    inventory.remove('key')
                    print('You reach for the key as you enter, but the key has vanished.')
                else:
                    print('Access to the Restricted Section is reserved to those with permission from the Headmaster.')
            # If player attempts to enter Headmaster's Office from stairs, they need the password
            elif currentRoom == 'Moving Staircases' and rooms[currentRoom][move[1]] == 'Headmaster\'s Office':
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

            # Check if player is attempting to enter dorm room - if so, prompt with riddle
            elif len(currentRoom.split(" ")) > 1 and currentRoom.split(" ")[1] == "CR" and rooms[currentRoom][move[1]].split(" ")[1] == "Dorm":
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
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')


