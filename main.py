from world.world import World
from agents.farmer import Farmer
from agents.lumberjack import Lumberjack
from agents.miner import Miner
from agents.merchant import Merchant
world = World()

# Inicializamos os agentes com algum dinheiro para o arranque da economia
world.add_agent(Farmer("Farmer1", 20))
world.add_agent(Farmer("Farmer2", 20))
world.add_agent(Lumberjack("Jack1", 30))
world.add_agent(Miner("Miner1", 30))

# Executa 50 dias para provar a estabilidade do novo modelo econômico
for _ in range(50):
    world.run_day()
    if len(world.agents) == 0:
        print("\n[COLAPSO ECONÓMICO] Todos os agentes morreram.")
        break

print("\n--- RESULTADO FINAL ---")
print(f"Agentes Vivos: {len(world.agents)}")
print(f"Dinheiro Total: {sum(a.money for a in world.agents)}")
print(f"Comida Total: {sum(a.food for a in world.agents)}")