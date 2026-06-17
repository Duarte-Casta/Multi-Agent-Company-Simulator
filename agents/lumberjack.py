from agents.base_agent import Agent

class Lumberjack(Agent):


    def act(self, world):

        if self.food < 2:
            self.buy_food(world)

        if self.energy < 5:
            self.food -= 1
            self.energy += 3
        
        if self.energy >= 3:
            self.wood += 2
            self.energy -= 3
        
        