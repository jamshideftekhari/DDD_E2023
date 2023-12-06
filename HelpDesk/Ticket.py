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
    
    def __str__(self):
        return self.title    