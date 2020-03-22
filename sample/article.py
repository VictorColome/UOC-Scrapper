class Article:

    def __init__(self):
        self.name = None
        self.price = 0.0
        self.pvp = 0.0
        self.discount = 0.0
        self.no_iva = 0.0
        self.rating = 0.0

    def set_price(self, price, cents):
        if cents is None:
            self.price = float(price)
        else:
            if "," in cents:
                self.price = float(price + cents.replace(',', '.'))
            else:
                self.price = float(price + cents)

    def __str__(self):
        return "Article: " + self.name + \
               "\n Price: " + str(self.price) + \
               "\n PVP: " + str(self.pvp) + \
               "\n Discount: " + str(self.discount) + \
               "\n No IVA: " + str(self.no_iva) + \
               "\n Rating: " + str(self.rating)
