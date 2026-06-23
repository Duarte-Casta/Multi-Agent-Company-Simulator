from agents.base_agent import Agent

class Farmer(Agent):
    def act(self, world):
        # Rede de segurança: Se o Farmer de alguma forma ficar sem comida, ele compra
        if self.food < 2:
            while self.food < 5 and self.money >= world.market.food_sell_price:
                self.buy_food(world)

        if self.rest_if_needed():
            return

        if self.energy >= 5:
            self.food += 3
            self.energy -= 2

        # Vende apenas o excedente seguro
        if self.food > 5:
            excess = self.food - 5
            self.sell_food(world, excess)