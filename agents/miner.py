from agents.base_agent import Agent


class Miner(Agent):

    def act(self, world):
        if self.energy > 0:
            self.coal += 2
            self.energy -= 1