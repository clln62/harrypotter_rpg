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