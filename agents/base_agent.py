
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
        if self.money >= world.market.food_sell_price:
            self.food += 1
            self.money -= world.market.food_sell_price

    def sell_wood(self, world, amount):
        amount = min(amount, self.wood)
        self.wood -= amount
        self.money += amount * world.market.wood_buy_price

    def sell_food(self, world, amount):
        amount = min(amount, self.food)
        self.food -= amount
        self.money += amount * world.market.food_buy_price

    def sell_coal(self, world, amount):
        amount = min(amount, self.coal)
        self.coal -= amount
        self.money += amount * world.market.coal_buy_price

    def rest_if_needed(self):
        # CORREÇÃO: Repousa se a energia cair abaixo ou igual a 5 
        # para garantir que nunca fica preso no "deadlock"
        if self.energy <= 5 and self.food > 0:
            self.food -= 1
            self.energy += 3
            return True
        return False

    def __str__(self):
        return (
            f"{self.name} | "
            f"Food:{self.food} | "
            f"Wood:{self.wood} | "
            f"Coal:{self.coal} | "
            f"Energy:{self.energy} | "
            f"Money:{self.money} | "
            f"Alive:{self.alive}"
        )