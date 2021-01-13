class Player:
    def __init__(self, name, inventory):
        self.health = 100
        self.name = name
        self.inventory = inventory



def new_player(inventory):
    print("What is your wizard name?")
    name = input(">").strip().upper()
    wizard = Player(name, inventory)
    return wizard


