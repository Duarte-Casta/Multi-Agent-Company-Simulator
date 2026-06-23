from world.market import Market


class World:
    def __init__(self):
        self.day = 0
        self.agents = []
        self.market = Market()

    def add_agent(self, agent):
        self.agents.append(agent)

    def run_day(self):
        self.day += 1
        self.agents = [a for a in self.agents if a.alive]
        print(f"\n--- Day {self.day} ---")

        for agent in self.agents:
            agent.act(self)

        for agent in self.agents:
            agent.consume_food()

        for agent in self.agents:
            print(agent)