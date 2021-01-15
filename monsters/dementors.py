from print_storyline import print_text

defeated = False

# If player defeats basilisk, set defeated to true
def dementors_defeated():
    global defeated
    defeated = True

def scenario1(player):
    print_text.print_text("""
You pull out your wand and hold it at the ready.
What spell will you cast to dispel of the dementors?
Enter "A" for Locomotor Wibbly to cause the dementors legs to collapse beneath them.
"B" for Nebulus to create a fog from the tip of your wand.
"C" for Expecto Patronum to cast a Patronus Charm filled with positive emotions.
"D" for Diffindo to send a cutting charm at the dementors.
    """)

    answer = input(">").strip().upper()

    if answer == 'A':
        print_text.print_text("""
Your spell shoots through the dementors as if nothing had happened.
A dementor comes from behind, knocking your wand from your hand and into a far away bush.
        """)
        loser()
    elif answer == 'B':
        scenario2(player)
    elif answer == 'C':
        expecto_patronum()
    elif answer == 'D':
        print_text.print_text("""
Your wand shoots a burst of light at one of the dementors, temporarily slowing it in its path to you.
A small piece of it's cloak cuts away and falls to the ground, but the dementor regains speed, sucking life away from you.
More dementors fly in to take away everything that you are, forcing you to slowly crumble.

GAME OVER
        """)
        return
    else:
        print_text.print_text("""
You miss your chance to cast a spell and a dementor knocks your wand away.
        """)
        loser()

def scenario2(player):
    print_text.print_text("""
A thick fog presses from the tip of your wand, filling the Training Field, so much so that you can no longer see the dementors.
One dementor claws at your back, cutting deep into your skin and causing you to fall to the ground.
Another dementor flies in to start sucking your life away. Darkness clouds around you, but you have enough strength for one last spell.

What spell will you cast to dispel of the dementors?
Enter "A" for Glacius to freeze the target with icy-cold air.
"B" for Expecto Patronum to cast a Patronus Charm filled with positive emotions.
"C" for Draconifors to transform your target into a dragon.
"D" for Wingardium Leviosa to make the dementors levitate.
            """)
    # Remove 10 points for scratch
    player.health -= 10

    answer = input(">").strip().upper()

    if answer == 'B':
        expecto_patronum()
    else:
        print_text.print_text("""
Your spell falls short, having no affect on the dementors.
One dementor knocks you to the ground, causing you to fall on top of your wand, snapping it in half.
        """)
        loser()


def expecto_patronum():
    print_text.print_text("""
    A burst of light shoots from your wand, holding off the dementors for a moment, but not sending them away.
    You struggle to hold the force of your wand as the dark creatures push against the light.
    Trying to remember your training and how to properly cast a Patronus Charm, you think about Harry Potter.

    Who saved Harry Potter from the dementors by the lake in Prisoner of Azkaban?
    Enter "A" for Albus Dumbledore
    "B" for Harry Potter's Father
    "C" for Sirius Black
    "D" for Harry Potter 
            """)

    answer = input(">").strip().upper()

    if answer == 'D':
        print_text.print_text("""
    Love and happiness builds within you, and you steady your hand and wand.
    You shout out 'Expecto Patronum' once more, casting out your patronus.
    Scouring away from the bouncing patronus, dementors disappear one-by-one.
    Light clears the dark sky, revealing an empty Training Field, and your patronus dances away, disappearing in the distance.
                """)
        dementors_defeated()
    else:
        print_text.print_text("""
    The light shooting from your want weakens more and more as dementors close in.
    Each time one of the dark creatures pass you, a piece of your life is sucked away.
    With strength dwindling, you drop your wand to the ground and fall to the ground.
    Dementors close in closer and closer until all of the light has dissipated.

    GAME OVER 
                """)

def loser():
    print_text.print_text("""
With no defenses, you trimmer in fear! Dementors sweep in to suck the life away from you.

GAME OVER
    """)
    return


def dementors_encountered(inventory, player):
    print_text.print_text("""
As you enter the Training Grounds, the light around you begins to slip away.
Happiness drains from you as fear shivers down the length of your spine.

From above, a group of dementors swirl around you, preventing a hasty escape.
You must be cleaver against these dark creatures, for only magic will force them to retreat.
    """)

    if 'wand' in inventory:
        scenario1(player)
    else:
        loser()
        return

    return defeated