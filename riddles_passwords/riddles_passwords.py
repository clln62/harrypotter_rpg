from print_storyline import print_text

# Password to gain access to Headmaster's Office
def headmasters_office():
    print_text.print_text("""
            What's the password?
            Enter "A" for Quidditch
            "B" for Sherbet Lemon
            "C" for Hocus Pocus
            "D" for Gillyweed
        """)

    answer = input(">").strip().upper()

    if answer == "B":
        return True
    else:
        print_text.print_text("\nThat is incorrect.")
        return False

def dorm_warning():
    print_text.print_text("""
In order to enter the house dorm, you must first answer this riddle. 
Answer correctly and you may enter. 
Answer incorrectly and face the consequences.
        """)

def dorm_answer():
    answer = input(">").strip().upper()
    return answer


def dorm_caught(professor):
    print_text.print_text(f"""
You have been caught by Professor {professor} for trying to sneak into another houses dorm!
They take you directly to the Headmaster's Office!
            """)


# To gain access to Gryffindor Dorm
def gryffindor_dorm():
    dorm_warning()
    print_text.print_text('''
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

    if dorm_answer() == 'D':
        return True
    else:
        dorm_caught("Minerva McGonagall")
        return False


# To gain access to Ravenclaw Dorm
def ravenclaw_dorm():
    dorm_warning()
    print_text.print_text('''
                Which came first, the phoenix or the flame?

                Enter "A" for phoenix. 
                "B" for flame. 
                "C" for weird question. 
                "D" for a circle has no beginning.
        ''')

    if dorm_answer() == 'D':
        return True
    else:
        dorm_caught("Filius Flitwick")
        return False


# To gain access to Slytherin Dorm
def slytherin_dorm():
    dorm_warning()
    print_text.print_text('''
                According to a Malfoy, what is more important than anything else?

                Enter "A" for magic. 
                "B" for pure-blood. 
                "C" for Tom Riddle. 
                "D" for Hogwarts.
        ''')

    if dorm_answer() == 'B':
        return True
    else:
        dorm_caught("Severus Snape")
        return False


# To gain access to Hufflepuff Dorm
def hufflepuff_dorm():
    dorm_warning()
    print_text.print_text('''
                There once was a kind woman that was known by all as Helga Hufflepuff.
                
                Here resides students inside her house.
                Tap the barrels, ounce by ounce.

                Enter "A" for [8, 5, 12, 7, 1, 8, 21, 6, 6, 12, 5, 16 21, 6, 6]
                "B" for [1, 12. 2. 21. 19. 4. 21. 13. 2. 12. 4. 15.18. 5]
                "C" for [23, 18, 15, 14, 7, 1, 14, 19, 23, 5, 18] 
                "D" for [8, 5, 1, 4, 13, 1, 19, 20, 5, 18, 19, 15, 6, 6, 9, 3, 5]
        ''')

    if dorm_answer() == 'A':
        return True
    else:
        dorm_caught("Pomonoa Sprout")
        return False
