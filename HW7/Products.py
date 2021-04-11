class Products:
    def __init__(self, product_type, product_name=0, price=0):
        self.product_type = product_type
        self.product_name = product_name
        self.price = price
        self.commission_groups = list()

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
