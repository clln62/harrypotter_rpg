defeated = False

# If player defeats basilisk, set defeated to true
def dementors_defeated():
    global defeated
    defeated = True

def scenario1(player):
    print("""
You pull out your wand and hold it at the ready.
What spell will you cast to dispel of the dementors?
Enter "A" for Locomotor Wibbly to cause the dementors legs to collapse beneath them.
"B" for Nebulus to create a fog from the tip of your wand.
"C" for Expecto Patronum to cast a Patronus Charm filled with positive emotions.
"D" for Diffindo to send a cutting charm at the dementors.
    """)

    print('---------------------------')
    answer = input(">").strip().upper()

    if answer == 'A':
        print("""
Your spell shoots through the dementors as if nothing had happened.
A dementor comes from behind, knocking your wand from your hand and into a far away bush.
        """)
        loser()
    elif answer == 'B':
        print("""
A thick fog presses from the tip of your wand, filling the Training Field, so much so that you can no longer see the dementors.
One dementor claws at your back, cutting deep into your skin and causing you to fall to the ground.

        """)
        player.health -= 10
        dementors_defeated()


def loser():
    print("""
    With no defenses, you trimmer in fear! Dementors sweep in to suck the life away from you.

    GAME OVER
    """)
    return


def dementors_encountered(inventory, player):
    print("""
As you enter the Training Grounds, the light around you begins to slip away.
Happiness drains from you as fear shivers down the length of your spine.

From above, a groups of dementors swirl around you, preventing a hasty escape.
You must be cleaver against these dark creatures, for only magic will for them to retreat.
    """)

    if 'wand' in inventory:
        scenario1(player)
    else:
        loser()
        return

    return defeated