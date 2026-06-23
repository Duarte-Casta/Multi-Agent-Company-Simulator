class Market:
    def __init__(self):
        #self.food_stock = 50
        #self.wood_stock = 0

        self.food_buy_price = 3   
        self.food_sell_price = 5  

        self.wood_buy_price = 3   
        self.wood_sell_price = 6  

        self.coal_buy_price = 3   
        self.coal_sell_price = 6

    def agent_sells_food(self, amount):
        self.food_stock += amount
        return amount * self.food_buy_price

    def agent_buys_food(self, amount):
        amount = min(amount, self.food_stock)
        self.food_stock -= amount
        return amount, amount * self.food_sell_price