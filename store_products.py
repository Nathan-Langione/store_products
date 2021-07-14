class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, sold_product):
        self.products.remove(sold_product)
        return self
    
    def list_products(self):
        print(f"{self.name} has the following products for sale")
        for i in range(len(self.products)):
            print(f"{self.products[i].__dict__}")
        print("\n")

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase)

    def set_clearance(self, category, percent_discount):
        for i in self.products:
            if i.category == "animal":
                i.update_price(percent_discount, False)


count = 0
class Products:
    def __init__(self, name, price, category):
        global count
        count += 1
        self.name = name
        self.price = price
        self.category = category
        self.id = count
        

    def update_price(self, percent_change, is_increased = True):
        if is_increased == True:
            self.price += (self.price * percent_change)
        else:
            self.price -= self.price *percent_change
        return self

    def print_info(self):
        print(f" Name: {self.name},  Category: {self.category}, Price: ${self.price}")
        return self

#stores        
stockyard = Store("Big Joes stockyard")
best_buy = Store("Best Buy")


#animals
duck = Products("duck",10,"animal")
cow = Products("cow",100,"animal")
chicken = Products("chicken",20,"animal")

#electronics
tv = Products("TV", 200,"electronics")
stereo = Products("Stereo", 100,"electronics")
dvd = Products("DVD Player", 50,"electronics")

#duck.print_info()
#cow.print_info()
#chicken.print_info()

#stockyard interaction
stockyard.add_product(cow).add_product(chicken).add_product(cow).add_product(duck)
stockyard.list_products()


chicken.update_price(0.1, False)
cow.update_price(0.1)
stockyard.sell_product(cow)
#stockyard.list_products()
stockyard.inflation(0.15)
#stockyard.list_products()
stockyard.set_clearance("animal",0.10)
stockyard.list_products()

""" #best buy interaction
best_buy.add_product(tv).add_product(dvd)
best_buy.list_products()
 """

