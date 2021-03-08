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


def calculator(total_price, discount, count, typ):
    if typ[0] == "Dollar":
        return round(total_price - discount[0] * count, 3)
    if typ[0] == "percent":
        return round(total_price * (1 - discount[0] / 100), 3)


def users_finder(group): return {group: index["users"] for index in discount_list
                                 if index["group_name"] == group}


def group_userid(part, group): return [index[part] for index in discount_list
                                       if index["group_name"] == group]


def calculate_product_price(product_type, count, userid):
    initial_price = [(1 + (calculate_markup_percent(product_type, count) / 100)) * index["price"]
                     for index in product_list if index["type"] == product_type]
    total_price = initial_price[0] * count
    set_of_whole_userid = set(numbers for index in discount_list for numbers in index["users"])
    if any([userid == number for number in set_of_whole_userid]):
        if all([any([userid == index for index in users_finder("A")["A"]]),
                any([product_type == index["type"] for index in product_list for
                     group in index["commission_groups"] if group == "A"])]):
            discount = group_userid("cost", "A")
            unit = group_userid("unit", "A")
            total_with_commission = calculator(total_price, discount, count, unit)
            discount_price = total_price - total_with_commission
        elif all([any([userid == index for index in users_finder("B")["B"]]),
                  any([product_type == index["type"] for index in product_list for
                       group in index["commission_groups"] if group == "B"])]):
            discount = group_userid("cost", "B")
            unit = group_userid("unit", "B")
            total_with_commission = calculator(total_price, discount, count, unit)
            discount_price = total_price - total_with_commission
        elif all([any([userid == index for index in users_finder("C")["C"]]),
                  any([product_type == index["type"] for index in product_list for
                       group in index["commission_groups"] if group == "C"])]):
            discount = group_userid("cost", "C")
            unit = group_userid("unit", "C")
            total_with_commission = calculator(total_price, discount, count, unit)
            discount_price = total_price - total_with_commission
        else:
            total_with_commission = total_price
            discount_price = total_price - total_with_commission
        return {
            "product_name": [index["name"] for index in product_list if index["type"] == product_type][0],
            "total_price": round(total_price, 3),
            "total_with_commission": round(total_with_commission, 3),
            "discount": round(discount_price, 3),
            "username": {
                "first_name": [index["first_name"] for index in user_list if index["userid"] == userid][0],
                "last_name": [index["last_name"] for index in user_list if index["userid"] == userid][0]
            }
        }
    else:
        return {
            "product_name": [index["name"] for index in product_list if index["type"] == product_type][0],
            "total_price": round(total_price, 3),
            "total_with_commission": round(total_price, 3),
            "discount": round(total_price, 3) - round(total_price, 3),
            "username": {
                "first_name": " ",
                "last_name": " "
            }
        }


print(calculate_product_price("1", 10, 1002))
