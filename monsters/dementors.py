defeated = False

# If player defeats basilisk, set defeated to true
def dementors_defeated():
    global defeated
    defeated = True

def scenario1():
    print("testing")

def dementors_encountered(inventory):
    print("""
As you enter the Training Grounds, the light around you begins to slip away.
Happiness drains from you as fear shivers down the length of your spine.

From above, a groups of dementors swirl around you, preventing a hasty escape.
You must be cleaver against these dark creatures, for only magic will for them to retreat.
    """)

    if 'wand' in inventory:
        scenario1()
    else:
        print("""
        With no defenses, you trimmer in fear! Dementors sweep in to suck the life away from you.
        
        GAME OVER
        """)
        return

    return defeated