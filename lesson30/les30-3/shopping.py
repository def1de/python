class Shop:
    def __init__(self, shop_name, shop_type, number_of_units, incremented):
        self.number_of_units = number_of_units
        self.shop_name = shop_name
        self.shop_type = shop_type
        self.incremented = incremented
    def describe_shop(self):
        print (f">>> {self.shop_name}\n>>> {self.shop_name}")
    def open_shop(self):
        print(f"Shop is open")
    def set_number_of_units(self):
        print(f"{self.number_of_units} units of product")
    def increment_number_of_units(self):
        self.number_of_units+=self.incremented
        print(f"New number of units is {self.number_of_units}")

class Discount(Shop):
    def __innit__(self, shop_name, shop_type, number_of_units=0):
        super().__init__(self, shop_name, shop_type, number_of_units=0)
        self.discount_products = ['product1', 'product2', 'product3']
    def get_discount_products(self):
        for i in self.discount_products:
            print(self.discount_products[i],)
