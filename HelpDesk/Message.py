
class Message():
    def __init__(self, message, user):
        self.message = message
        self.user = user

    def __str__(self):
        return str(self.user) + ": " + str(self.message)