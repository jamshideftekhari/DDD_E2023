from Message import Message

messages = []
domainEvents = []

class Ticket():
    def __init__(self, ticket_id, title, description, status, priority, user_id, created_at, updated_at):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at

    # commands 
    def AddMessage(self, from_user_id, message):
        m = Message(message, from_user_id) 
        self.messages.append(m)  
        return m

    # domain events
    def MessageAdded(self, message):
        self.domainEvents.append(message)

    def EscalateAdd(self, event):
        self.domainEvents.append(event)    
    

    """The code snippet is for a class called "Ticket". 
    Inside this class, there is a list variable called "_messages" which holds instances of the "Message" class. 
    The code snippet also includes a method called "Execute" which takes a parameter of type "AcknowledgeMessage". 
    Inside the method, there is a line of code that finds a message from the list based on its "Id" property
    matching the one passed in the "AcknowledgeMessage" parameter.
    Once the message is found, the code marks the "WasRead" property of that message as true, indicating that it has been read."""

    def execute(self, cmd):
        message = next((x for x in self._messages if x.id == cmd.id), None)
        if message:
            message.was_read = True

    """This code is a part of a class called "Ticket". 
    The class has a private list called "_domainEvents" which stores objects of type "DomainEvent". 
    The code snippet shows a method called "Execute" which takes a parameter of type "RequestEscalation". 
    Inside the method, there is an if statement that checks two conditions. 
    The first condition checks if the ticket is not already escalated and the second condition checks if the remaining 
    time percentage is less than or equal to 0. If both conditions are true, then the code proceeds to execute the statements 
    inside the if block. 
    It sets the "IsEscalated" property of the ticket object to true and creates a new object of type "TicketEscalated" with the 
    given parameters "_id" and "cmd.Reason". Finally, it appends the newly created "escalatedEvent" object to the "_domainEvents" list."""
    def execute(self, cmd):
        if not self.is_escalated and self.remaining_time_percentage <= 0:
            self.is_escalated = True
            escalated_event = TicketEscalated(self._id, cmd.reason)
            self._domainEvents.append(escalated_event)

    def __str__(self):
        return self.title    