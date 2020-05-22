import re

def get_locations():
    with open("./data/locations.txt", "r") as f:
        locations = f.read()
        return locations.split("\n")

def get_cities():
    with open("./data/cities.txt", "r") as f:
        cities = f.read()
        return cities.split("\n")

def get_pokemon():
    with open("./data/pokemon.txt", "r") as f:
        pokemon = f.read()
        return pokemon.split("\n")

def get_moves():
    with open("./data/moves.txt", "r") as f:
        moves = f.read()
        return moves.split("\n")

def get_abilities():
    with open("./data/abilities.txt", "r") as f:
        abilities = f.read()
        return abilities.split("\n")

def get_items():
    with open("./data/items.txt", "r") as f:
        items = f.read()
        return items.split("\n")

def get_side_locations():
    with open("./data/Side Game Locations.txt", "r") as f:
        items = f.read()
        items_lst = items.split("\n")
        return [x for x in items_lst if not x.startswith("#")]

class resolver():
    def __init__(self, Type):
        if Type.lower() == "location":
            self.active_list = get_locations()
        elif Type.lower() == "city":
            self.active_list = get_cities()
        elif Type.lower() == "pokemon":
            self.active_list = get_pokemon()
        elif Type.lower() == "item":
            self.active_list = get_items()
        elif Type.lower() == "move":
            self.active_list = get_moves()
        elif Type.lower() == "ability":
            self.active_list = get_abilities()
        elif Type.lower() == "side":
            self.active_list = get_side_locations()

    def feed(self, hint):
        regex = re.compile("^"+hint+"$", re.IGNORECASE)
        
        self.active_list = [item for item in self.active_list if bool(regex.match(item))]

        if len(self.active_list) == 1:
            return self.active_list[0]
