import random


class Player:
    def __init__(self, name, gender, pokemon_list, bag, money):
        self.name = name
        self.gender = gender
        self.pokemon_list = pokemon_list
        self.bag = bag
        self.money = money
        self.x = 0
        self.y = 0


class Potion:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Pokemon:
    def __init__(self, name, gender, moves, health, max_health):
        self.name = name
        self.gender = gender
        self.moves = moves
        self.health = max_health
        self.max_health = max_health

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


pokemon_pool = ["Charmander", "Pikachu","Piplup","Ratatta","Bellsprout","Geodude","Pidgey","Gastly","Krabby"]


class Moves:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power


move_pool1 = [Moves("Tackle", 40), Moves("Pound", 40), Moves("Stomp", 50), Moves("Slap", 20)]
move_pool2 = [Moves("Nothing", 0), Moves("Dance", 0), Moves("Sing", 0), Moves("Stare", 0)]
move_pool3 = [Moves("Flamewheel", 60), Moves("Thunder Punch", 90), Moves("Blizzard", 100), Moves("Shadow Ball", 80)]


class Trainer:
    def __init__(self, name, pokemon_list, money, fun_fact):
        self.name = name
        self.pokemon_list = pokemon_list
        self.money = money
        self.fun_fact = fun_fact
    def __repr__(self):
        return "T"

    def __str__(self):
        return "T"


trainer_pool = ["John", "May", "Red", "Ash", "Rose", "Mike"]
fun_fact_pool = [" likes fishing", " likes cooking", " likes swimming", " likes biking", " likes balling"]

class GridTile:
    def __init__(self, occupant, symbol):
        self.symbol = symbol
        self.occupant = occupant

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.actual_grid = []

    def render(self):


        initial_grid = self.actual_grid

        for row in range(self.width):
            initial_grid.append([])
            for column in range(self.height):
                tile = random.choice([GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile("none", "-"),
                                      GridTile(Potion("Potion", 40), "I"),
                                      GridTile(Potion("Super Potion", 60), "I"),
                                      GridTile(Pokemon(random.choice(pokemon_pool), random.choice(["male", "female"]),
                                                       [random.choice(move_pool1), random.choice(move_pool2),
                                                        random.choice(move_pool3)], 0, random.randint(70, 120)), "P"),
                                      GridTile(Pokemon(random.choice(pokemon_pool), random.choice(["male", "female"]),
                                                       [random.choice(move_pool1), random.choice(move_pool2),random.choice(move_pool3)], 0, random.randint(70, 120)), "P"),
                                      GridTile(Trainer(random.choice(trainer_pool),
                                                        [Pokemon(random.choice(pokemon_pool), random.choice(["male", "female"]), [random.choice(move_pool1), random.choice(move_pool2), random.choice(move_pool3)], 0, random.randint(70, 120)),
                                                        Pokemon(random.choice(pokemon_pool), random.choice(["male", "female"]), [random.choice(move_pool1), random.choice(move_pool2), random.choice(move_pool3)], 0, random.randint(70, 120))],
                                                        random.randint(1000, 10000), random.choice(fun_fact_pool)), "T")
                ])



                initial_grid[-1].append(tile)

        return initial_grid

    def display(self):
        for row in self.actual_grid:
            print(row)

    def update(self, Player, command):
        initial_grid = self.actual_grid

        initial_grid[Player.x][Player.y] = GridTile("none", "-")

        # move up
        if command.lower() == "a":
            if Player.y - 1 < 0:
                print("Out of bounds! Move somewhere else")
            else:
                Player.y = Player.y - 1
        # move left
        if command == "w":
            if Player.x - 1 < 0:
                print("Out of bounds! Move somewhere else")
            else:
                Player.x = Player.x - 1
        # move down
        if command == "d":
            if Player.y + 1 >= len(initial_grid):
                print("Out of bounds! Move somewhere else")
            else:
                Player.y = Player.y + 1
        # move right
        if command == "s":
            if Player.x + 1 >= len(initial_grid):
                print("Out of bounds! Move somewhere else")
            else:
                Player.x = Player.x + 1
        if command == "p":
            print("Pokemon: " + str(Player.pokemon_list))

        if command == "b":
            print("Bag: " + str(Player.bag))

        if command == "m":
            print("Money: $" + str(Player.money))

        if initial_grid[Player.x][Player.y].symbol == "P":
            battle(Player, [initial_grid[Player.x][Player.y].occupant], "pokemon",
                   initial_grid[Player.x][Player.y].occupant)

            for p in Player.pokemon_list:
                p.health = p.max_health

        if initial_grid[Player.x][Player.y].symbol == "T":
            battle(Player, initial_grid[Player.x][Player.y].occupant.pokemon_list, "trainer",
                   initial_grid[Player.x][Player.y].occupant)

            for p in Player.pokemon_list:
                p.health = p.max_health

        if initial_grid[Player.x][Player.y].symbol == "I":
            Player.bag.append(initial_grid[Player.x][Player.y].occupant)
            print("Found " + initial_grid[Player.x][Player.y].occupant.name + "!")

        initial_grid[Player.x][Player.y] = GridTile(Player, "x")

        return initial_grid


def battle(player, opponent, type, occupant):
    i = 0
    j = 0

    if type == "pokemon":
        print("Wild " + occupant.name + " appeared!")
    if type == "trainer":
        print(occupant.name + " challenges you to a battle!")

    while i < len(player.pokemon_list):

        print("Your " + player.pokemon_list[i].name + " (" + str(
            player.pokemon_list[i].health) + " hp) is fighting against the opposing " + opponent[j].name + " (" + str(
            opponent[j].health) + " hp)")
        command = input("\nWhat will you do?\nF for Fight, B for Bag, R for Run\n")

        if command == "f":
            for move_name in player.pokemon_list[i].moves:
                print(move_name.name)

            move = input("\nChoose a move (1-4)\n")
            opponent[j].health = opponent[j].health - player.pokemon_list[i].moves[int(move) - 1].attack_power
            print("Used " + player.pokemon_list[i].moves[int(move) - 1].name + "! Opposing " + opponent[
                j].name + " took " + str(player.pokemon_list[i].moves[int(move) - 1].attack_power) + " damage")

            if opponent[j].health <= 0:
                print("Opposing " + opponent[j].name + " fainted! \n")
                j = j + 1

                if j >= len(opponent):
                    print("You win!")
                    if type == "pokemon":
                        print(opponent[j - 1].name + " has joined your party.")
                        player.pokemon_list.append(opponent[j - 1])

                    if type == "trainer":
                        player.money = player.money + occupant.money
                        print(occupant.name + " gives you " + str(occupant.money) + " dollars")
                        print(occupant.name + occupant.fun_fact)
                        # funfact
                    return

            opponent_move = random.choice(opponent[j].moves)
            player.pokemon_list[i].health = player.pokemon_list[i].health - opponent_move.attack_power
            print("Opposing " + opponent[j].name + " used " + opponent_move.name + "! Your " + player.pokemon_list[
                i].name + " took " + str(opponent_move.attack_power) + " damage\n")

            if player.pokemon_list[i].health <= 0:
                print("Your " + player.pokemon_list[i].name + " fainted!\n")
                i = i + 1

        if command == "r":
            if type == "trainer":
                print("Can't Run!\n")
            if type == "pokemon":
                print("Ran away!\n")
                break
        if command == "b":
            if not player.bag:
                print("Bag is empty")
            else:
                print(str(player.bag) + "\n")
                item = input("Choose an Item (1-" + str(len(player.bag)) + ")\n")

                if player.pokemon_list[i].health + player.bag[int(item) - 1].health > player.pokemon_list[i].max_health:
                    player.pokemon_list[i].health = player.pokemon_list[i].max_health
                else:
                    player.pokemon_list[i].health = player.pokemon_list[i].health + player.bag[int(item) - 1].health

                del player.bag[int(item) - 1]
    print("You lost!")

if __name__ == '__main__':
    # init grid
    my_grid = Grid(8, 8)
    my_grid.render()

    # init player
    name = input("What is your name?\n")
    gender = input("What is your gender?\n")
    starters = ["Snivy", "Tepig", "Oshawatt"]
    starter = input("Choose a starter (1, 2, 3)\nSnivy, Tepig, Oshawatt\n")
    my_player = Player(name, gender, [Pokemon(starters[int(starter) - 1], random.choice(["male", "female"]),
                                              [random.choice(move_pool1), random.choice(move_pool2),random.choice(move_pool3)], 0,
                                              random.randint(80, 120))], [], 10000)
    my_grid.actual_grid[0][0] = GridTile(my_player, "x")

    my_grid.display()  # print after ever update

    while True:
        command = input("Enter a command (WASD, P (Pokemon), B (Bag), M (Money) E (End Game)\n")  # wasd
        if command == "e":
            print("Thanks for playing!\n")
            break
        my_grid.update(my_player, command)
        my_grid.display()
