

class Agent:
    def __init__(self, name, money=100):
        self.name = name
        self.money = money

        self.food = 5
        self.wood = 0
        self.coal = 0

        self.energy = 10
        self.alive = True

    def consume_food(self):
        if self.food > 0:
            self.food -= 1
        else:
            self.energy -= 2

        if self.energy <= 0:
            self.alive = False


    def buy_food(self, world):
        if self.money >= world.market.food_price:
            self.food += 1
            self.money -= world.market.food_price

    def __str__(self):
        return (
            f"{self.name} | "
            f"Food:{self.food} | "
            f"Wood:{self.wood} | "
            f"Coal:{self.coal} | "
            f"Energy:{self.energy}"
        )