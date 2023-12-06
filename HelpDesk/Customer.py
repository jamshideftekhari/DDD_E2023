class Customer():
    def __init__(self, name, address, phone, cardNumber, cardType, cardExpiry):
        self.name = name
        self.address = address
        self.phone = phone
        self.cardNumber = cardNumber
        self.cardType = cardType
        self.cardExpiry = cardExpiry

    def __str__(self):
        return self.name

    def NumberCheck(self):
        if self.cardNumber == 0:
            return False
        return True