class Markup:
    def __init__(self, product_type, lower_count, lower_cost, upper_cost):
        self.product_type = product_type
        self.lower_count = lower_count
        self.lower_cost = lower_cost
        self.upper_cost = upper_cost
        self.count = 0

    def get_product_type(self):
        return self.product_type

    def get_markup_percent(self, count):
        self.count = count
        coefficient_markup = round(((self.lower_cost - self.upper_cost) * self.count + (
                (self.lower_count * self.upper_cost) - self.lower_cost)) / (self.lower_count - 1), 3)
        if self.count <= self.lower_count:
            return coefficient_markup
        else:
            return self.lower_cost
