

class World:
    def __init__(self):
        self.day = 0
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def run_day(self):
        self.day += 1

        print(f"\n--- Day {self.day} ---")

        for agent in self.agents:
            agent.act(self)

        for agent in self.agents:
            agent.consume_food()

        for agent in self.agents:
            print(agent)