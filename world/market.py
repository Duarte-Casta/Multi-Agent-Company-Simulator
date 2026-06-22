class Market:
    def __init__(self):
        self.food_stock = 50
        self.wood_stock = 0

        self.food_buy_price = 5
        self.food_sell_price = 6

    def agent_sells_food(self, amount):
        self.food_stock += amount
        return amount * self.food_buy_price

    def agent_buys_food(self, amount):
        amount = min(amount, self.food_stock)
        self.food_stock -= amount
        return amount, amount * self.food_sell_price