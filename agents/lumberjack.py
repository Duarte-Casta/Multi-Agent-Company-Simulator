from agents.base_agent import Agent

class Lumberjack(Agent):
    def act(self, world):
        if self.energy > 0:
            self.wood += 2
            self.energy -= 1