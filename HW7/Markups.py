class Markup:
    markup_info = dict()

    def __init__(self, product_type, lower_count, lower_cost, upper_cost):
        self.product_type = product_type
        self.lower_count = lower_count
        self.lower_cost = lower_cost
        self.upper_cost = upper_cost
        Markup.markup_info[self.product_type] = {"lower_count": self.lower_count,
                                                 "lower_cost": self.lower_cost, "upper_cost": self.upper_cost}

    def get_product_type(self):
        return self.product_type


type_1 = Markup("1", 10, 10, 20)
type_2 = Markup("2", 10, 15, 20)
type_3 = Markup("3", 5, 10, 15)
type_4 = Markup("4", 20, 10, 30)
