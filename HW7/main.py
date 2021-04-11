from Products import Products
from Markups import Markup
from Discounts import Discounts
from Userid import Userid
from CashDesk import CashDesk
from pprint import pprint

shirt = Products("1", "shirt", 30)
shirt.add_commission_groups("A")
shirt.add_commission_groups("B")
pants = Products("2", "pants", 50)
pants.add_commission_groups("A")
pants.add_commission_groups("C")
shoes = Products("3", "shoes", 80)
shoes.add_commission_groups("B")
hat = Products("4", "hat", 20)

mohsen_bayat = Userid("Mohsen", "Bayat", 1001)
sobhan_taghadosi = Userid("Sobhan", "Taghadosi", 1002)
javad_jafari = Userid("Javad", "Jafari", 1003)
masoud_hosseini = Userid("Masoud", "Hosseini", 1004)
hassan_zand = Userid("Hassan", "Zand", 1005)
ali_ebadi = Userid("Ali", "Ebadi", 1006)

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

type_1 = Markup("1", 10, 10, 20)
type_2 = Markup("2", 10, 15, 20)
type_3 = Markup("3", 5, 10, 15)
type_4 = Markup("4", 20, 10, 30)

# --------------------problem 1--------------------
type_4.get_markup_percent(8)
type_3.get_markup_percent(20)
type_2.get_markup_percent(1)
type_1.get_markup_percent(5)

pprint(type_1.get_markup_percent(5))

# --------------------problem 2--------------------
buyer = CashDesk("4", 20, 1005)
member_ids = [mohsen_bayat.get_user_id(), sobhan_taghadosi.get_user_id(), javad_jafari.get_user_id(),
              masoud_hosseini.get_user_id(), hassan_zand.get_user_id(), ali_ebadi.get_user_id()]

full_name_members = {mohsen_bayat.get_user_id(): [mohsen_bayat.get_first_name(), mohsen_bayat.get_last_name()],
                     sobhan_taghadosi.get_user_id(): [sobhan_taghadosi.get_first_name(),
                                                      sobhan_taghadosi.get_last_name()],
                     javad_jafari.get_user_id(): [javad_jafari.get_first_name(), javad_jafari.get_last_name()],
                     masoud_hosseini.get_user_id(): [masoud_hosseini.get_first_name(), masoud_hosseini.get_last_name()],
                     hassan_zand.get_user_id(): [hassan_zand.get_first_name(), hassan_zand.get_last_name()],
                     ali_ebadi.get_user_id(): [ali_ebadi.get_first_name(), ali_ebadi.get_last_name()]}

products = {shirt.get_product_type(): [shirt.get_product_name(), shirt.get_commission_groups(), shirt.get_price()],
            pants.get_product_type(): [pants.get_product_name(), pants.get_commission_groups(), pants.get_price()],
            shoes.get_product_type(): [shoes.get_product_name(), shoes.get_commission_groups(),
                                       shoes.get_price()],
            hat.get_product_type(): [hat.get_product_name(), hat.get_commission_groups(), hat.get_price()]}

markup_product = {type_1.get_product_type(): type_1.get_markup_percent(buyer.get_count()),
                  type_2.get_product_type(): type_2.get_markup_percent(buyer.get_count()),
                  type_3.get_product_type(): type_3.get_markup_percent(buyer.get_count()),
                  type_4.get_product_type(): type_4.get_markup_percent(buyer.get_count())}

discount_info = {a_group.get_group_name(): [a_group.get_users(), a_group.get_info()],
                 b_group.get_group_name(): [b_group.get_users(), b_group.get_info()],
                 c_group.get_group_name(): [c_group.get_users(), c_group.get_info()]}

discount_list = products[buyer.get_product_type()][1]
is_a_member = list()
for number in member_ids:
    is_a_member.append(buyer.get_id_number() == number)
price_list = list()
total_price = round(products[buyer.get_product_type()][2] * buyer.get_count() * (
        1 + markup_product[buyer.get_product_type()] / 100), 3)
for group in discount_list:
    for number in discount_info[group][0]:
        if buyer.get_id_number() == number:
            if discount_info[group][1][0] == "percent":
                total_price_with_commission = round(total_price * (1 - discount_info[group][1][1] / 100), 3)
                price_list.append(total_price_with_commission)
            elif discount_info[group][1][0] == "Dollar":
                total_price_with_commission = round(total_price - discount_info[group][1][1], 3)
                price_list.append(total_price_with_commission)

if any(is_a_member):
    first_name, last_name = full_name_members[buyer.get_id_number()][0], full_name_members[buyer.get_id_number()][1]
else:
    first_name, last_name = "", ""

if discount_list:
    pprint({
        "product_name": products[buyer.get_product_type()][0],
        "total_price": total_price,
        "total_price_with_commission": min(price_list),
        "discount": total_price - min(price_list),
        "username": {
            "first_name": first_name,
            "last_name": last_name
        }
    })
else:
    pprint({
        "product_name": products[buyer.get_product_type()][0],
        "total_price": total_price,
        "total_price_with_commission": total_price,
        "discount": total_price - total_price,
        "username": {
            "first_name": first_name,
            "last_name": last_name
        }
    })
