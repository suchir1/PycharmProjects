import numpy as np

class Player:
    board_dict = {0: ['Go'], 1: ['Purple', 60, 2, 10, 30, 90, 160, 250], 2: ['Community Chest'],
                  3: ['Purple', 60, 4, 20, 60, 180, 320, 450], 4: ['Income Tax'], 5: ['Railroad', 200],
                  6: ['Light-Blue', 100, 6, 30, 90, 270, 400, 550], 7: ['Chance'],
                  8: ['Light-Blue', 100, 6, 30, 90, 270, 400, 550], 9: ['Light-Blue', 120, 8, 40, 100, 300, 450, 600],
                  10: ['Jail'], 11: ['Violet', 140, 10, 50, 150, 450, 625, 750], 12: ['Utilities', 150],
                  13: ['Violet', 140, 10, 50, 150, 450, 625, 750], 14: ['Violet', 160, 12, 60, 180, 500, 700, 900],
                  15: ['Railroad', 200], 16: ['Orange', 180, 14, 70, 200, 550, 750, 950], 17: ['Community Chest'],
                  18: ['Orange', 180, 14, 70, 200, 550, 750, 950], 19: ['Orange', 200, 16, 80, 220, 600, 800, 1000],
                  20: ['Free Parking'], 21: ['Red', 220, 18, 90, 250, 700, 875, 1050], 22: ['Chance'],
                  23: ['Red', 220, 18, 90, 250, 700, 875, 1050], 24: ['Red', 240, 20, 100, 300, 750, 925, 1100],
                  25: ['Railroad', 200], 26: ['Yellow', 260, 22, 110, 330, 800, 975, 1150],
                  27: ['Yellow', 260, 22, 110, 330, 800, 975, 1150], 28: ['Utilities', 150],
                  29: ['Yellow', 280, 24, 120, 360, 850, 1025, 1200], 30: ['Go to Jail'],
                  31: ['Dark-Green', 300, 26, 130, 390, 900, 1100, 1275],
                  32: ['Dark-Green', 300, 26, 130, 390, 900, 1100, 1275], 33: ['Community Chest'],
                  34: ['Dark-Green', 320, 28, 150, 450, 1000, 1200, 1400], 35: ['Railroad', 200], 36: ['Chance'],
                  37: ['Dark-Blue', 350, 35, 175, 500, 1100, 1300, 1500], 38: ['Luxury Tax'],
                  39: ['Dark-Blue', 400, 50, 200, 600, 1400, 1700, 2000]}

    ownership_dict = {0: ['', 0], 1: ['', 0], 2: ['', 0], 3: ['', 0], 4: ['', 0], 5: ['', 0], 6: ['', 0], 7: ['', 0], 8: ['', 0], 9: ['', 0], 10: ['', 0], 11: ['', 0], 12: ['', 0], 13: ['', 0], 14: ['', 0], 15: ['', 0], 16: ['', 0], 17: ['', 0], 18: ['', 0], 19: ['', 0], 20: ['', 0], 21: ['', 0], 22: ['', 0], 23: ['', 0], 24: ['', 0], 25: ['', 0], 26: ['', 0], 27: ['', 0], 28: ['', 0], 29: ['', 0], 30: ['', 0], 31: ['', 0], 32: ['', 0], 33: ['', 0], 34: ['', 0], 35: ['', 0], 36: ['', 0], 37: ['', 0], 38: ['', 0], 39: ['', 0]}


    def __init__(self, name, buy_chance):
        self.name = name
        self.percent_chance_to_buy = buy_chance
        self.money = 1500
        self.position = 0
        self.jailed = False

    def is_jailed(self):
        return self.jailed

    def print_money(self):
        print(self.money)

    def print_pos(self):
        print(self.position)

    def roll(self):
        all_rolls = []
        if self.jailed:
            roll1 = np.random.randint(1, 7)
            roll2 = np.random.randint(1, 7)
            if roll1 == roll2:
                all_rolls.append(roll1 + roll2)
                self.jailed = False
            else:
                return []

        doubles = True
        i = 0
        while doubles:
            doubles = False
            if i ==3:
                self.jailed = True
                return []
            roll1 = np.random.randint(1, 7)
            roll2 = np.random.randint(1, 7)
            if roll1==roll2:
                all_rolls.append(roll1 + roll2)
                doubles = True
                i+=1
            else:
                all_rolls.append(roll1 + roll2)
                return all_rolls

    def move(self, list):
        if self.money <= 0:
            list.remove(self)
        roll = self.roll()
        if self.jailed or not roll:
            return
        new_pos = []
        for individual_roll in roll:
            new_pos.append(self.position + individual_roll)
        if max(new_pos) >= 40:
            self.money += 200
        for element in new_pos:
            element = element % 40
            self.position = element
            self.interact_with_tile()

    def interact_with_tile(self):
        if len(Player.board_dict[self.position]) <=2:
            self.interact_with_special_tile()
            return
        else:
            return


    def interact_with_special_tile(self):
        return


    def make_bankrupt(self):
        self.money = 0





player_list = []
players_completed = False

while not players_completed:
    player_list.append(Player(input("What is your name? "), input("What percent chance to buy?")))
    if input("Finished? y/n") == "y":
        players_completed = True



for i in range(1, 1000):
    for player in player_list:
        player.move(player_list)

for player in player_list:
    player.print_pos()
    player.print_money()

print(Player.ownership_dict)