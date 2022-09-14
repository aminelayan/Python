class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self,id):
        print("Product is:")
        self.products[id].print_info()
        del self.products[id]
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
            return self

    def set_clearance(self, percent_discount):
        for product in self.products:
            product.update_price(percent_discount, False)
            return self

class Product:
  def __init__(self, name, price, category):
    self.name = name
    self.price = price
    self.category = category

  def update_price(self, percent_change, is_increased):
    if is_increased:
      self.price += self.price * percent_change
    elif not is_increased:
      self.price -= self.price * percent_change
      print("Product name:", self.name, "\n", "Category:",
            self.category, "\n", "Price: $ ", self.price, "\n", f"-" * 100)
    return self

  def print_info(self):
    print("Product name:", self.name, "\n", "Category:",
          self.category, "\n", "Price: $ ", self.price, "\n", f"-"*100)
    return self

amin = Store(name="Amin")
steak=Product(name="Ribeye", price=25, category="Meat")
cola=Product(name="Coca Cola", price=1, category="Drinks")
molikhia=Product(name="Molkhia", price=5, category="Vegatabels")
sprite=Product(name="Sprite", price=1, category="Drinks")
cerelac=Product(name="Cerelac",price=7,category="Baby Food")

amin.add_product(steak).add_product(cola).add_product(molikhia).add_product(sprite).add_product(cerelac).inflation(0.5)
cerelac.print_info()
cerelac.update_price(0.5,True)
amin.sell_product(4)



