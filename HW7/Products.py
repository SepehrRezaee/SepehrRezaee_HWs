class Products:
    products_info = dict()

    def __init__(self, product_type, product_name, price):
        self.product_type = product_type
        self.product_name = product_name
        self.price = price
        self.commission_groups = list()
        Products.products_info[self.product_type] = {"product_name": self.product_name,
                                                     "commission_groups": self.commission_groups,
                                                     "price": self.price}

    def get_price(self):
        return self.price

    def get_product_type(self):
        return self.product_type

    def get_product_name(self):
        return self.product_name

    def add_commission_groups(self, group_name):
        self.commission_groups.append(group_name)

    def get_commission_groups(self):
        return self.commission_groups

    def __repr__(self):
        return Products.products_info


shirt = Products("1", "shirt", 30)
shirt.add_commission_groups("A")
shirt.add_commission_groups("B")
pants = Products("2", "pants", 50)
pants.add_commission_groups("A")
pants.add_commission_groups("C")
shoes = Products("3", "shoes", 80)
shoes.add_commission_groups("B")
hat = Products("4", "hat", 20)
