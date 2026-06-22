from world.world import World
from agents.farmer import Farmer
from agents.lumberjack import Lumberjack
from agents.miner import Miner
from agents.merchant import Merchant
world = World()

world.add_agent(Farmer("Farmer1", 10))
world.add_agent(Farmer("Farmer2", 10))
world.add_agent(Lumberjack("Jack1", 10))

for _ in range(100):
    world.run_day()

alive = len(world.agents)

total_food = sum(a.food for a in world.agents)
total_money = sum(a.money for a in world.agents)
total_wood = sum(a.wood for a in world.agents)

print(
    f"Alive:{alive} "
    f"Food:{total_food} "
    f"Money:{total_money} "
    f"Wood:{total_wood} "
)