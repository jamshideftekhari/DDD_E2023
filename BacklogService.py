# pattern 1 transaction script - simple business logic
#transaction script for backlog for intergrating with repository (storage mecanism)
#trasactions should either succeed or fail completely

class BacklogService:
    def __init__(self, backlogRepository):
        self.backlogRepository = backlogRepository

    def getBacklog(self, backlogId):
        return self.backlogRepository.getBacklog(backlogId)

    def getBacklogs(self):
        return self.backlogRepository.getBacklogs()

    def createBacklog(self, backlog):
        return self.backlogRepository.createBacklog(backlog)

    def updateBacklog(self, backlog):
        return self.backlogRepository.updateBacklog(backlog)

    def deleteBacklog(self, backlogId):
        return self.backlogRepository.deleteBacklog(backlogId)