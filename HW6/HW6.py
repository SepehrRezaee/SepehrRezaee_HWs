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


def calculator_of_total_with_commission(total_price, discount_number, count, type_of_unit):
    if type_of_unit[0] == "Dollar":
        return round(total_price - discount_number[0] * count, 3)
    if type_of_unit[0] == "percent":
        return round(total_price * (1 - discount_number[0] / 100), 3)


def comparator(total_price, count, group_names_type):
    total_with_commission = list()
    for group_name in group_names_type:
        discount_number = finder_values_of_discount_list("cost", group_name)
        type_of_unit = finder_values_of_discount_list("unit", group_name)
        total_with_commission.append(
            calculator_of_total_with_commission(total_price, discount_number, count, type_of_unit))
    return max(total_with_commission)


def finder_values_of_discount_list(part_of_dict, group_name):
    return [dictionary[part_of_dict] for dictionary in discount_list
            if dictionary["group_name"] == group_name]


def codes_of_users(group): return [numbers for lists in discount_list for numbers in lists["users"]
                                   if lists["group_name"] == group]


def repetition(group_names_of_product_type, userid):
    counter = 0
    for group in group_names_of_product_type:
        for numbers in codes_of_users(group):
            if numbers == userid:
                counter += 1
    return counter

# --------------------problem 2--------------------
def calculate_product_price(product_type, count, userid):
    initial_price = [(1 + (calculate_markup_percent(product_type, count) / 100)) * index["price"]
                     for index in product_list if index["type"] == product_type]
    total_price = initial_price[0] * count
    whole_userid = [index["userid"] for index in user_list]
    group_names_of_product_type = [names for index in product_list for names in index["commission_groups"]
                                   if index["type"] == product_type]
    if all([any([userid == number for number in whole_userid]), len(group_names_of_product_type) != 0]):
        if repetition(group_names_of_product_type, userid) == 0:
            total_with_commission = total_price
            discount = total_price - total_with_commission
        elif repetition(group_names_of_product_type, userid) == 1:
            discount_number = finder_values_of_discount_list("cost", group_names_of_product_type[0])
            unit = finder_values_of_discount_list("unit", group_names_of_product_type[0])
            total_with_commission = calculator_of_total_with_commission(total_price, discount_number, count, unit)
            discount = total_price - total_with_commission
        else:
            total_with_commission = comparator(total_price, count, group_names_of_product_type)
            discount = total_price - total_with_commission
        return {
            "product_name": [index["name"] for index in product_list if index["type"] == product_type][0],
            "total_price": round(total_price, 3),
            "total_with_commission": round(total_with_commission, 3),
            "discount": round(discount, 3),
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
                "first_name": [index["first_name"] if index["userid"] == userid else "" for index in user_list][0],
                "last_name": [index["last_name"] if index["userid"] == userid else "" for index in user_list][0]
            }
        }


print(calculate_product_price("1", 10, 1002))
