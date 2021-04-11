class Discounts:
    def __init__(self, group_name, cost, unit):
        self.group_name = group_name
        self.cost = cost
        self.unit = unit
        self.user_ids = list()
        self.info_dict = dict()

    def add_users(self, id_number):
        self.user_ids.append(id_number)

    def get_users(self):
        return self.user_ids

    def get_group_name(self):
        return self.group_name

    def get_unit(self):
        return self.unit

    def get_cost(self):
        return self.cost

    def get_info(self):
        return [self.get_unit(), self.get_cost()]
