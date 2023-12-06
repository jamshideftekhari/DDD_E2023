# each massage instantiates a domain service response time object
class ResponseTime:
    def __init__(self, response_time):
        self.response_time = response_time

    def get_response_time(self):
        return self.response_time

    def set_response_time(self, response_time):
        self.response_time = response_time


class TicketScalation():
    def __init__(self, EscalationLevel):
        self.EscalationLevel = EscalationLevel

    def get_EscalationLevel(self):
        return self.EscalationLevel

    def set_EscalationLevel(self, EscalationLevel):
        self.EscalationLevel = EscalationLevel    

    def __str__(self):
        return self.title        