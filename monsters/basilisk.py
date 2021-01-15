defeated = False


# If player defeats basilisk, set defeated to true
def basilisk_defeated():
    global defeated
    defeated = True


def scenario1(player, inventory):
    # Continue to take damage until sword or wand is chosen
    while True:

        print("""
The basilisk turns towards you, ready to strike.
Will you grab your sword or wand?
Enter "A" for sword.
"B" for wand.
        """)

        print('---------------------------')
        answer = input(">").strip().upper()

        if answer == 'A':
            scenario3(player, inventory)
            break
        elif answer == 'B':
            scenario2(player,inventory)
            break
        else:
            print("""
You fail to grab your sword or wand.
The basilisk barrels into you, hurling you across the room and crashing into a sculpture.
            """)
            player.health -= 25


def scenario2(player, inventory):
    print("""
With your wand pointed at the speeding basilisk, you cast a spell.
Enter "A" for Melofors to encase the basilisk head in a pumpkin.
"B" for Colovaria to change the color of the serpent.
"C" for Condundo to confuse and befuddle the basilisk.
"D" for Crucio to inflict intense paine on the basilisk.
        """)

    print('---------------------------')
    answer = input(">").strip().upper()

    if answer == 'A':
        print("""
A pumpkin covers the basilisk's head, causing it to change course and crash into a wall.
The tail of the creature swings and knocks the wind out of you. You suffer 10 points of damage.
        """)
        player.health -= 10
        if 'sword' in inventory:
            print("""
Will you cast another spell, or will you brandish your sword?
Enter "A" for spell.
"B" for sword.
            """)

            print('---------------------------')
            answer = input(">").strip().upper()

            if answer == 'A':
                scenario2(player, inventory)
            elif answer == 'B':
                scenario3(player, inventory)

    elif answer == 'B':
        print("""
Your spell performs all too well, causing the basilisk's color to blend more with the surrounding.
Almost impossible to see, the serpent crashes into you, forcing you against a wall and crushing your insides.

GAME OVER
        """)
        return
    elif answer == 'C':
        print("Your spell works, confusing the basilisk and causes it to move in a different direction.")
        if 'sword' in inventory:
            print("""
Will you cast another spell, or will you brandish your sword?
Enter "A" for spell.
"B" for sword.
            """)

            print('---------------------------')
            answer = input(">").strip().upper()

            if answer == 'A':
                scenario2(player, inventory)
            elif answer == 'B':
                scenario3(player, inventory)
    elif answer == 'D':
        print("""
Choosing the dark-side to perform an unforgivable curse, you direct your wand directly at the basilisk.
The creature screams in pain, swinging its head uncontrollably in an attempt to remove the pain.
Crashing into walls and the ceiling, it is clear that the basilisk has gone mad.
You witness the destruction of the room until it all comes to a stop when the basilisk throws its head into a sharp, stone point on the ceiling.
The basilisk falls to the ground, motionless and defeated.      
        """)
        basilisk_defeated()
        return


def scenario3(player, inventory):
    print("""
You swing your sword as the basilisk approaches, causing it to hesitate in strategy on how to attack.
What is your next move?
Enter "A" to run away from basilisk.
"B" to attack the basilisk head on.
"C" to hide back under desk.
    """)

    print('---------------------------')
    answer = input(">").strip().upper()

    if answer == 'A':
        print("""
You make a run for it, but the basilisk is quicker than you, taking a chunk from your arm as it snips. You suffer 25 points in damage.
Ahead, there is a ceiling too low for the basilisk at its current speed.
        """)
        player.health -= 25
        if 'wand' in inventory:
            print("""
What will you do next?
Enter "A" to continue with sword.
"B" to switch to your wand.
            """)

            print('---------------------------')
            answer = input(">").strip().upper()

            if answer == 'B':
                scenario2(player, inventory)
            else:
                sword_winning(player)
        else:
            sword_winning(player)

    elif answer == 'B':
        print("""
Your bravery carries to head on to the basilisk. You slide across the floor to avoid a strike, cutting into the side of the creature.
The basilisk is swift at turning around to face you again. You are now trapped in a corner.
        """)

        if 'wand' in inventory:
            print("""
What will you do next?
Enter "A" to stand strong with your sword.
"B" to pull out your wand for some magic.
            """)

            print('---------------------------')
            answer = input(">").strip().upper()

            if answer == 'B':
                scenario2(player, inventory)
            else:
                print("""
You see a small opening to a room with a ceiling that is too low for the basilisk at a swift speed.
You make a run for it, barely clearing the next room before the basilisk hits the wall.
                """)
                sword_winning(player)
        else:
            print("""
You see a small opening to a room with a ceiling that is too low for the basilisk at a swift speed.
What will you do?
Enter "A" to make a run for the room.
"B" to face the basilisk head on.
            """)

            print('---------------------------')
            answer = input(">").strip().upper()

            if answer == 'A':
                print("You make a run for it, barely clearing the next room before the basilisk hits the wall.")
                sword_winning(player)
            else:
                print("""
You make a grave mistake in trying to face the basilisk head on, as you have nowhere to jump away from attacks.
Your bravery is strong as you run at the creature, but the basilisk is too quick for you to attack.
The basilisk knocks the sword from your hand, leaving you defenseless in a corner.

GAME OVER
                """)
                return

    elif answer == 'C':
        print("""
You quickly hide under the desk, but the basilisk saw your every move.
The dark creature barrels towards you, destroying everything in its path.
In a last moment of bravery, you attempt to come out with the sword, but it slips from your hand.
The basilisk is swift in its strike.

GAME OVER
        """)
        return


def sword_winning(player):
    print("""
The basilisk enters the room, and is ready to kill.
From a hidden corner, you jump on the neck of the lowered basilisk and sink your sword into the back of its head.
In agony, the beast throws you off it's back and into a wall, flailing about the room.
With a tremendous amount of blood loss, the basilisk weakens until it cannot stand anymore.
You suffer 20 points of damage, but you have defeated the basilisk.
                    """)
    player.health -= 20
    basilisk_defeated()
    return

def basilisk_encountered(inventory, player):
    print("""
You quickly reach for the door behind you, but the door has vanished, leaving no exit.
The gigantic basilisk, slithers across the room and opens its mouth with a hiss.
You slide under a desk, barely avoiding the deadly bite of the serpent.
You must act quickly if you wish to survive!
    """)

    if 'wand' in inventory and 'sword' in inventory:
        scenario1(player, inventory)
    elif 'wand' in inventory:
        scenario2(player, inventory)
    elif 'sword' in inventory:
        scenario3(player, inventory)
    else:
        print("""
        With no defenses, you trimmer in fear, only to be eaten whole by the basilisk.
        
        GAME OVER
                """)
    if defeated:
        print("The door you came in through has returned.")
    return defeated


# **********************************
# Add a way for player to open the door again to exit at the end
