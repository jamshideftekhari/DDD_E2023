"""This code snippet is defining a class called "AnalysisModelProjection". 
It has several properties: LeadId, Followups, Status, and Version. 
These properties have private setters, which means they can only be set within the class. 
The class also has several methods called "Apply". 
Each method corresponds to a specific event, such as "LeadInitialized", "Contacted", "FollowupSet", etc. 
These events represent different actions or changes that can occur in the system. 
Each "Apply" method updates the properties of the class based on the specific event it corresponds to. 
For example, the "Apply(LeadInitialized @event)" method sets the LeadId, Followups, Status, and Version properties to specific values 
when a "LeadInitialized" event occurs. 
Other "Apply" methods increment the Version property by 1 and update the Status property based on the specific event. 
Overall, this code snippet is defining a class that can update its properties based on different events that occur in the system. 
This class is likely used to track and analyze the progress of leads in a sales or marketing system."""


class AnalysisModelProjection:
    def __init__(self):
        self.LeadId = 0
        self.Followups = 0
        self.Status = ''
        self.Version = 0

    def Apply(self, event):
        if isinstance(event, LeadInitialized):
            self.LeadId = event.LeadId
            self.Followups = 0
            self.Status = 'NEW_LEAD'
            self.Version = 0
        elif isinstance(event, Contacted):
            self.Version += 1
        elif isinstance(event, FollowupSet):
            self.Status = 'FOLLOWUP_SET'
            self.Followups += 1
            self.Version += 1
        elif isinstance(event, ContactDetailsChanged):
            self.Version += 1
        elif isinstance(event, OrderSubmitted):
            self.Status = 'PENDING_PAYMENT'
            self.Version += 1
        elif isinstance(event, PaymentConfirmed):
            self.Status = 'CONVERTED'
            self.Version += 1