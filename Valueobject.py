class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class Customer:
    def __init__(self, name, address, phone, cardNumber, cardType, cardExpiry):
        self.name = name
        self.address = address
        self.phone = phone
        self.cardNumber = cardNumber
        self.cardType = cardType
        self.cardExpiry = cardExpiry

class CreditCardType:
    def __init__(self, number, type, expiry):
        self.number = number
        self.type = type
        self.expiry = expiry

    def __str__(self):
        return self.type
     
    def NumberCheck(self):
        if self.number == 0:
            return False
        return True