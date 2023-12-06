#wraps a row in the database, encapsulate access to the database, and adds domain logic on that data.
#complex data structures from the database are converted to native python data types - no flat data structures

class user():
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

class CreateUser():
    def __init__(self, user):
        self.user = user

    def execute(self, userDetails):
        #if user exists, return false
        #else create user and return true
        try:
            _db.SratTrasaction()  #start transaction not implemented
            self.user.id = userDetails['id']
            self.user.name = userDetails['name']
            self.user.email = userDetails['email']
            self.user.password = userDetails['password']
            _db.save(self.user) #save not implemented
            _db.commit() #commit not implemented

        except KeyError:
            _db.rollback() #rollback not implemented
            return False

        return True        