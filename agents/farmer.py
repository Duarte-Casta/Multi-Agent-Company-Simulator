from agents.base_agent import Agent

class Farmer(Agent):
    def act(self, world):
        if self.energy > 0:
            self.food += 3
            self.energy -= 1