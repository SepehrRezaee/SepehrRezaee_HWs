class CashDesk:
    def __init__(self, product_type, count, id_number):
        self.id_number = id_number
        self.count = count
        self.product_type = product_type
        self.checker = list()

    def get_product_type(self):
        return self.product_type

    def get_id_number(self):
        return self.id_number

    def get_count(self):
        return self.count
