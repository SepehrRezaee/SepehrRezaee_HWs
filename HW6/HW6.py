product_list = [
    {
        "type": "1",
        "name": "shirt",
        "price": 30,
        "unit": "Dollar",
        "commission_groups": ["A", "B"]
    },
    {
        "type": "2",
        "name": "pants",
        "price": 50,
        "unit": "Dollar",
        "commission_groups": ["A", "C"]
    },
    {
        "type": "3",
        "name": "shoes",
        "price": 80,
        "unit": "Dollar",
        "commission_groups": ["B"]
    },
    {
        "type": "4",
        "name": "hat",
        "price": 20,
        "unit": "Dollar",
        "commission_groups": []
    }
]

markup_list = [
    {
        "product_type": "1",
        "lower_cost": 10,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "2",
        "lower_cost": 15,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "3",
        "lower_cost": 10,
        "upper_cost": 15,
        "unit": "percent",
        "lower_count": 5
    },
    {
        "product_type": "4",
        "lower_cost": 10,
        "upper_cost": 30,
        "unit": "percent",
        "lower_count": 20
    },
]

discount_list = [
    {
        "group_name": "A",
        "cost": 5,
        "unit": "percent",
        "users": [1001, 1002, 1003, 1005]
    },
    {
        "group_name": "B",
        "cost": 3,
        "unit": "Dollar",
        "users": [1001, 1003, 1006]
    },
    {
        "group_name": "C",
        "cost": 7,
        "unit": "percent",
        "users": [1001, 1002, 1004]
    }
]

user_list = [
    {
        "userid": 1001,
        "first_name": "Mohsen",
        "last_name": "Bayat",
    },
    {
        "userid": 1002,
        "first_name": "Sobhan",
        "last_name": "Taghadosi",
    },
    {
        "userid": 1003,
        "first_name": "Javad",
        "last_name": "Jafari",
    },
    {
        "userid": 1004,
        "first_name": "Masoud",
        "last_name": "Hosseini",
    },
    {
        "userid": 1005,
        "first_name": "Hassan",
        "last_name": "Zand",
    },
    {
        "userid": 1006,
        "first_name": "Ali",
        "last_name": "Ebadi",
    }
]


# --------------------problem 1--------------------
def calculate_markup_percent(typ, count):
    upper_cost = [index["upper_cost"]
                  for index in markup_list if index["product_type"] == typ]
    lower_cost = [index["lower_cost"]
                  for index in markup_list if index["product_type"] == typ]
    lower_count = [index["lower_count"]
                   for index in markup_list if index["product_type"] == typ]
    if count <= lower_count[0]:
        coefficient_markup = float(
            ((lower_cost[0] - upper_cost[0]) * count + ((lower_count[0] * upper_cost[0]) - lower_cost[0])) /
            (lower_count[0] - 1))
    else:
        coefficient_markup = lower_cost[0]
    return round(coefficient_markup, 3)


def comparator(total_price, group_names_type, group_name_userid):
    total_with_commission = list()
    for group in group_names_type:
        for name in group_name_userid:
            if name == group:
                discount_number = finder_values_of_discount_list("cost", group)
                type_of_unit = finder_values_of_discount_list("unit", group)
                total_with_commission.append(
                    calculator_of_total_with_commission(total_price, discount_number, type_of_unit))
    return min(total_with_commission)


def finder_values_of_discount_list(part_of_dict, group_name):
    return [dictionary[part_of_dict] for dictionary in discount_list
            if dictionary["group_name"] == group_name]


def calculator_of_total_with_commission(total_price, discount_number, type_of_unit):
    if type_of_unit[0] == "Dollar":
        return round(total_price - discount_number[0], 3)
    elif type_of_unit[0] == "percent":
        return round(total_price * (1 - discount_number[0] / 100), 3)


# --------------------problem 2--------------------
def calculate_product_price(product_type, count, userid):
    total_price = [(1 + (calculate_markup_percent(product_type, count) / 100)) * index["price"]
                   for index in product_list if index["type"] == product_type][0] * count
    group_names_of_product_type = [name for index in product_list for name in index["commission_groups"]
                                   if index["type"] == product_type]
    group_name_userid = [index["group_name"] for index in discount_list
                         for numbers in index["users"] if numbers == userid]
    if any([userid == number["userid"] for number in user_list]):
        first_name = [index["first_name"] for index in user_list if index["userid"] == userid]
        last_name = [index["last_name"] for index in user_list if index["userid"] == userid]
        if len(group_names_of_product_type) != 0:
            total_with_commission = comparator(total_price, group_names_of_product_type, group_name_userid)
            discount = total_price - total_with_commission
        else:
            total_with_commission = total_price
            discount = total_price - total_with_commission
    else:
        first_name = last_name = [""]
        total_with_commission = total_price
        discount = total_price - total_with_commission
    return {
        "product_name": [index["name"] for index in product_list if index["type"] == product_type][0],
        "total_price": round(total_price, 3),
        "total_with_commission": round(total_with_commission, 3),
        "discount": round(discount, 3),
        "username": {
            "first_name": first_name[0],
            "last_name": last_name[0]
        }
    }


print(calculate_product_price("4", 20, 1005))
