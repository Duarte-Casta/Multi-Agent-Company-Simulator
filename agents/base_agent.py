class Agent:
    def __init__(self, name, money=100):
        self.name = name
        self.money = money
        self.food = 5
        self.wood = 0
        self.energy = 10

    def act(self, world):
        pass

    def consume_food(self):
        if self.food > 0:
            self.food -= 1
        else:
            self.energy -= 2
    
    def __str__(self):
        return f"{self.name} | Money: {self.money} | Food: {self.food} | Wood: {self.wood} | Energy: {self.energy}"