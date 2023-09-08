"""
The idea is to build a square matrix containing zeroes and we will place a battleship randomly on the grid.

The user has a few chances to drop a bomb on the location of the ship by guessing. After a few incorrect guesses, the game will be over.
"""
import random

class Ship:
    def __init__(self, length):
        self.x = random.randint(0, length-1)
        self.y = random.randint(0, length-1)
        self.out = False
    def reroll(self, length):
        self.x = random.randint(0, length-1)
        self.y = random.randint(0, length-1)
    


def print_battle_field(battle_field):
    for row in range(0, len(battle_field)):
        for col in range(0, len(battle_field[row])):
            print(battle_field[row][col], end=" ")
        print("\n")

battle_field = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

lives = 3
has_won = False
length = 3
print("There are two ships you need to take down: ")
print("Enter the row and col: ")
ship_one = Ship(length)
ship_two = Ship(length)

while ship_one.x == ship_two.x and ship_one.y == ship_two.y:
    ship_one.reroll(length)
    ship_two.reroll(length)

print("There are two ships you need to take down: ")
print("You must enter the row and col: ")
print_battle_field(battle_field)

while lives > 0:
    if ship_one.out == True and ship_two.out == True:
        has_won = True
        break
    print(f"Lives: {lives}")
    try:
        user_row = int(input("Enter row: ")) -1
        user_col = int(input("Enter col: ")) -1
        if user_row == ship_one.x and user_col == ship_one.y:
            battle_field[user_row][user_col] = 1
            print_battle_field(battle_field)
            ship_one.out = True
        elif user_row == ship_two.x and user_col == ship_two.y:
            battle_field[user_row][user_col] = 1
            print_battle_field(battle_field)
            ship_two.out = True
        else:
            battle_field[user_row][user_col] = -1
            print_battle_field(battle_field)
            lives -= 1
    except:
        print(f"You must enter an integer 1 through {length}")

if has_won == True:
    print("You have won")
else:
    print("You have lost")
    print(f"Ship one ({ship_one.x + 1}, {ship_one.y + 1}) and Ship Two ({ship_two.x +1 }, {ship_two.y + 1})")