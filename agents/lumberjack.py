from agents.base_agent import Agent

class Lumberjack(Agent):

    def act(self, world):

        if self.wood >= 5:
            self.sell_wood(world, 5)

        if self.food < 5:
            while self.food < 5 and self.money >= world.market.food_sell_price:
                self.buy_food(world)

        if self.energy < 5 and self.food > 0:
            self.food -= 1
            self.energy += 3
            return

        if self.energy >= 3:
            self.wood += 2
            self.energy -= 3
        
        