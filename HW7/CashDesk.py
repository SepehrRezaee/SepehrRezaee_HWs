class CashDesk:
    def __init__(self, product_type, count, id_number, member_ids, fullname_members):
        self.product_type = product_type
        self.count = count
        self.id_number = id_number
        self.member_ids = member_ids
        self.fullname_members = fullname_members
        self.checker = list()

    def is_a_member(self):
        self.checker = []
        for number in self.member_ids:
            self.checker.append(number == self.id_number)
        return any(self.checker)

    def get_first_name(self):
        if self.is_a_member():
            return self.fullname_members[self.get_id_number()][0]
        else:
            return ""

    def get_last_name(self):
        if self.is_a_member():
            return self.fullname_members[self.get_id_number()][1]
        else:
            return ""

    def get_product_type(self):
        return self.product_type

    def get_id_number(self):
        return self.id_number

    def get_count(self):
        return self.count
