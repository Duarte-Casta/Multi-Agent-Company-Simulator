from world.world import World
from agents.farmer import Farmer
from agents.lumberjack import Lumberjack
from agents.miner import Miner
from agents.merchant import Merchant
world = World()

world.add_agent(Farmer("Farmer1", 10))
world.add_agent(Farmer("Farmer2", 10))
world.add_agent(Lumberjack("Jack1", 10))

for _ in range(10):
    world.run_day()