class Article:

    def __init__(self, name=None, price=0.0, no_iva=0.0, pvp=0.0, discount=0.0, rating=0.0, features=None):
        self.name = name
        self.price = price
        self.pvp = pvp
        self.discount = discount
        self.no_iva = no_iva
        self.rating = rating
        self.features = features

    def __str__(self):
        return "Article: " + self.name + \
               "\n Price: " + str(self.price) + \
               "\n PVP: " + str(self.pvp) + \
               "\n Discount: " + str(self.discount) + \
               "\n No IVA: " + str(self.no_iva) + \
               "\n Rating: " + str(self.rating) + \
               "\n Features: " + str(self.features)
