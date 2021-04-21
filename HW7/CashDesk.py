from Discount import Discounts
from Markups import Markup
from Products import Products
from Userids import Userid


class CashDesk:
    def __init__(self, product_type, count, id_number=None):
        self.product_type = product_type
        self.count = count
        self.id_number = id_number
        self.checker = list()
        self.price_list = list()

    def is_a_member(self):
        for number in Userid.member_ids:
            self.checker.append(number == self.id_number)
        return any(self.checker)

    def get_first_name(self):
        if self.is_a_member():
            return Userid.member_info[self.id_number]["first_name"]
        else:
            return ""

    def get_last_name(self):
        if self.is_a_member():
            return Userid.member_info[self.id_number]["last_name"]
        else:
            return ""

    def get_markup_percent(self):
        coefficient_markup = round(((Markup.markup_info[self.product_type]["lower_cost"] -
                                     Markup.markup_info[self.product_type]["upper_cost"]) * self.count + (
                                            (Markup.markup_info[self.product_type]["lower_count"] *
                                             Markup.markup_info[self.product_type]["upper_cost"]) -
                                            Markup.markup_info[self.product_type]["lower_cost"])) / (
                                           Markup.markup_info[self.product_type]["lower_count"] - 1), 3)
        if self.count <= Markup.markup_info[self.product_type]["lower_count"]:
            return coefficient_markup
        else:
            return Markup.markup_info[self.product_type]["lower_cost"]

    def get_total_price(self):
        return round(
            Products.products_info[self.product_type]["price"] * self.count * (1 + self.get_markup_percent() / 100), 3)

    def get_list_total_price_with_commission(self):
        for group in Products.products_info[self.product_type]["commission_groups"]:
            for number in Discounts.discounts_info[group]["user_ids"]:
                if self.id_number == number:
                    if Discounts.discounts_info[group]["unit"] == "percent":
                        self.price_list.append(round(
                            self.get_total_price() * (1 - Discounts.discounts_info[group]["cost"] / 100), 3))
                    elif Discounts.discounts_info[group]["unit"] == "Dollar":
                        self.price_list.append(round(
                            self.get_total_price() - Discounts.discounts_info[group]["cost"], 3))
        return self.price_list

    def get_total_price_with_commission(self):
        if self.is_a_member():
            return round(min(self.get_list_total_price_with_commission()), 3)
        else:
            return self.get_total_price()

    def get_product_type(self):
        return self.product_type
