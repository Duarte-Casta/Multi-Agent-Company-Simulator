from agents.base_agent import Agent

class Farmer(Agent):
    def act(self, world):
        if self.food > 0 and self.energy < 5:
            self.food -= 1
            self.energy += 3
            return

        if self.energy >= 5:
            self.food += 3
            self.energy -= 2