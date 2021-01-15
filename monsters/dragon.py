from print_storyline import print_text

defeated = False

# If player defeats dragon, make sure to make correct updates where needed
def dragon_defeated():
    global defeated
    defeated = True


# If player has wand, sword and broom, this function gets called
def scenario1(inventory, player):
    print_text.print_text("""
With your wand at the ready, you must come up with a spell to distract the dragon!
Enter "A" for Aqua Eructo to shoot a stream of water at the dragon.
"B" for Langlock to stick the dragon's tongue to the tip of its mouth.
"C" fo Flipendo to knock the dragon backwards
    """)
    answer = input('>').strip().upper()

    # If they select the correct spell, they are taken on a winning path against the dragon
    if answer == "A":
        print_text.print_text("""
Like a firehose, water bursts from the tip of your wand, forcing the dragon towards the corner of the room.
You know that charms and jinx won't penetrate the dragon's thick skin, so you must be clever.
        """)
        if 'broom' in inventory:
            print_text.print_text("""
You swiftly use the Accio summoning charm to call your broom, mounting it.
Flying around the dragon, you confuse it with your speed, giving you time to brandish your sword.
You fly below the belly of the dragon, thrusting your sword into the stomach of the creature.
Just as you clear the dragon above you, it stumbles to the ground, its body shaking the ground and walls.
Beyond the tail of the dragon, you can now see the exit. 
            """)
            dragon_defeated()
        else:
            scenario2(player)
    # Any other spell will fail, causing more effort to win against the dragon
    # This scenario is not yet completed
    else:
        scenario3(player)


# This gets called if player does not have the broom
def scenario2(player):
    print_text.print_text("""
Three spells come to your mind:
Enter "A" for Defodio to dig and carve through the dragon.
"B" for Moblicorpus to levitate and move the dragon.
"C" for Wingardium Leviosa to levitate a large rock onto the dragon.
    """)

    answer = input('>').strip().upper()

    # winning spell
    if answer == 'C':
        print_text.print_text("""
You cast Wingardium Leviosa to the largest rock you can see, causing the rock smash into the dragon.
The dragon falls to the ground, shaking its head from the blunt of the rock.
With spared time, you brandish your sword, jabbing it into the side of the dragon.
It swats you away, causing you to take on 25 points of damage when you hit a wall.
Luckily for you, the sword was enough to cause the dragon to bleed out, giving you access to an exit.
        """)
        player.health -= 25
        dragon_defeated()
    # Other spells fail and the player loses
    else:
        print_text.print_text("""
When it is too late, you remember that your spell cannot penetrate the skin of the dragon.
The dragon breathes fire onto your hand, knocking your wand away.
You reach for your sword, but the dragon is too quick, moving its flames to your other hand.
You become overwhelmed in the fire with no other options.
\nGAME OVER
        """)
        return


# This scenario is unfinished, but will be called if the player calls a failing spell from the start
def scenario3(player):
    print_text.print_text("""
You cast a spell at the dragon, but it cannot penetrate the dragon's skin and fails to work.
Aggravated, the dragon swings its tail and knocks you to the ground. Your wand flies through the air.
You take 10 points of damage.
    """)
    player.health -= 10

    print_text.print_text("""
With no way to cast spells, you are left with your sword to defend yourself.
What will you do?
Enter "A" to make a run for your wand.
"B" to attack with your sword.
    """)

    answer = input('>').strip().upper()

    if answer == 'A':
        print_text.print_text("""
You dive and roll in the direction of your wand, narrowly avoiding a grab from the dragon.
You land inches from your wand and pick it up just in time.        
        """)
        scenario2(player)
    else:
        fail_no_wand()


def fail_no_sword():
    print_text.print_text("""
You raise your wand, but as you are about to cast your first spell, the dragon knocks you to the ground.
Your wand snaps as you fall to the hard ground.
The dragon takes a deep breath, letting out one last burst of flames.

GAME OVER
    """)
    return


def fail_no_wand():
    print_text.print_text("""
You jump to action, brandishing your sword. 
The dragon flaps its wings in intimidation, shaking the ground beneath you as it lands.
You take a swing at the dragons stomach, but you are too close and too slow.
The dragon opens its mouth, swiftly wrapping it around your head.

GAME OVER
    """)
    return


# This function will be called from main once player comes across the dragon
def dragon_encountered(inventory, player):
    print_text.print_text("""
The magnificent dragon flaps its wings and blows fire in your direction.
You narrowly jump out of the way of the burning flames.
You must act quickly if you wish to survive!
                """)
    # Player can only win with both sword and wand
    if 'wand' in inventory and 'sword' in inventory:
        scenario1(inventory, player)
    # without a sword, the wizard has no means to win
    elif 'wand' in inventory:
        fail_no_sword()
    # without a wand, the wizard cannot get close enough to the dragon to use the sword
    elif 'sword' in inventory:
        fail_no_wand()
    # would you fight a dragon with nothing but your hands?
    else:
        print_text.print_text("""
With no defenses, you trimmer in fear, only to be engulfed by the flames of the dragon.
\nGAME OVER
        """)
    return defeated

