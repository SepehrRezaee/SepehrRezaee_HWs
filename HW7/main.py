from Products import Products
from CashDesk import CashDesk
from pprint import pprint

# --------------------problem 1--------------------
example = CashDesk("1", 15)
pprint(example.get_markup_percent())
# --------------------problem 2--------------------
buyer = CashDesk("1", 15, 1003)

pprint({"product_name": Products.products_info[buyer.get_product_type()]["product_name"],
        "total_price": buyer.get_total_price(),
        "total_price_with_commission": buyer.get_total_price_with_commission(),
        "discount": buyer.get_total_price() - buyer.get_total_price_with_commission(),
        "username": {
            "first_name": buyer.get_first_name(),
            "last_name": buyer.get_last_name()
        }
        })
