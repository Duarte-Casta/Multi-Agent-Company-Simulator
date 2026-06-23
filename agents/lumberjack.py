from agents.base_agent import Agent

class Lumberjack(Agent):
    def act(self, world):
        # Garante comida antes de tentar trabalhar
        if self.food < 3:
            while self.food < 5 and self.money >= world.market.food_sell_price:
                self.buy_food(world)

        if self.rest_if_needed():
            return

        if self.energy >= 3:
            self.wood += 2
            self.energy -= 3

        if self.wood > 0:
            self.sell_wood(world, self.wood)