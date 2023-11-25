#basket=[]
#basket=[{"Product":"Leather wallet",
#         "Unit_price":1100,
#         "GST":18,
#         "Quantity":1},
#
#         {"Product":"Umbrella",
#         "Unit_price":900,
#         "GST":12,
#         "Quantity":4},
#
#         {"Product":"Cigarette",
#         "Unit_price":200,
#         "GST":28,
#         "Quantity":3},
#
#         {"Product":"Honey",
#         "Unit_price":100,
#         "GST":0,
#         "Quantity":2}]

class Product:
    def __init__(self, product, unit_price, gst, quantity):
        self.product = product
        self.unit_price = unit_price
        self.gst = gst
        self.quantity = quantity

    def calculate_total_bill(self):
        return (self.unit_price + (self.unit_price * self.gst / 100)) * self.quantity
    
leather_wallet = Product("Leather Wallet", 1100, 18, 1)
umbrella = Product("Umbrella", 900, 12, 4)
cigarette = Product("Cigarette", 200, 28, 3)
honey = Product("Honey", 100, 0, 2)

basket = [leather_wallet, umbrella, cigarette, honey]

max_gst = max(basket, key=lambda a: (a.unit_price * a.gst / 100) * a.quantity)
print(f"Product for which we paid maximum GST amount: {max_gst.product}")

total_bill = sum(product.calculate_total_bill() for product in basket)
print(f"Total amount to be paid to the shop-keeper: Rs. {total_bill}")