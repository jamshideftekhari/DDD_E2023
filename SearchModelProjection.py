class LeadSearchModelProjection:
    def __init__(self):
        self.LeadId = None
        self.FirstNames = set()
        self.LastNames = set()
        self.PhoneNumbers = set()
        self.Version = 0

    def Apply(self, event):
        if isinstance(event, LeadInitialized):
            self.LeadId = event.LeadId
            self.FirstNames = set()
            self.LastNames = set()
            self.PhoneNumbers = set()
            self.FirstNames.add(event.FirstName)
            self.LastNames.add(event.LastName)
            self.PhoneNumbers.add(event.PhoneNumber)
            self.Version = 0
        elif isinstance(event, ContactDetailsChanged):
            self.FirstNames.add(event.FirstName)
            self.LastNames.add(event.LastName)
            self.PhoneNumbers.add(event.PhoneNumber)
            self.Version += 1
        elif isinstance(event, Contacted):
            self.Version += 1
        elif isinstance(event, FollowupSet):
            self.Version += 1
        elif isinstance(event, OrderSubmitted):
            self.Version += 1
        elif isinstance(event, PaymentConfirmed):
            self.Version += 1
