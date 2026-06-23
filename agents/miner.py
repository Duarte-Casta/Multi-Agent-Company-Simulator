from agents.base_agent import Agent

class Miner(Agent):
    def act(self, world):
        if self.food < 3:
            while self.food < 5 and self.money >= world.market.food_sell_price:
                self.buy_food(world)

        if self.rest_if_needed():
            return

        if self.energy >= 3:
            self.coal += 2
            self.energy -= 3

        if self.coal > 0:
            self.sell_coal(world, self.coal)