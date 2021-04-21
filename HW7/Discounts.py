class Discounts:
    discounts_info = dict()

    def __init__(self, group_name, cost, unit):
        self.group_name = group_name
        self.cost = cost
        self.unit = unit
        self.user_ids = list()
        Discounts.discounts_info[self.group_name] = {"cost": self.cost, "unit": self.unit, "user_ids": self.user_ids}

    def add_users(self, id_number):
        self.user_ids.append(id_number)

    def get_group_name(self):
        return self.group_name

    def get_unit(self):
        return self.unit

    def get_cost(self):
        return self.cost

    def __repr__(self):
        return Discounts.discounts_info


a_group = Discounts("A", 5, "percent")
a_group.add_users(1001)
a_group.add_users(1002)
a_group.add_users(1003)
a_group.add_users(1005)
b_group = Discounts("B", 3, "Dollar")
b_group.add_users(1001)
b_group.add_users(1003)
b_group.add_users(1006)
c_group = Discounts("C", 7, "percent")
c_group.add_users(1001)
c_group.add_users(1002)
c_group.add_users(1004)
