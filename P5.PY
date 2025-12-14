class shoppingcart:
    def __init__(self):
        self.items = []
        
    def add_item(self,name,price):
        self.items.append((name,price))
        
    def total_price(self):
        return sum(price for name,price in self.items)

cart = shoppingcart()
cart.add_item("Bag",500)
cart.add_item("shoes",2000)
cart.add_item("jacket",2000)
print("total_price:", cart.total_price())