from agents.base_agent import Agent

class Farmer(Agent):
    def act(self, world):
        # Recupera energia
        if self.food > 0 and self.energy < 5:
            self.food -= 1
            self.energy += 3
            return

        if self.energy >= 5:
            self.food += 3
            self.energy -= 2

        if self.food > 10:
            excess = self.food - 10
            self.food -= excess
            self.money += excess * world.market.food_buy_price