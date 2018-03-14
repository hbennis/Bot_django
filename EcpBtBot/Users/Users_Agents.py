from .Member import Member
class Users_Agents(object):
    """Contains the connected members and their requested agents"""
    def __init__(self):
        self.members={}

    def connectMember(self,userid):
        if not userid in self.members:
            self.addConnectMember(userid)

    def addConnectMember(self, userid):
        user=Member(userid)
        self.members[userid] = user

    def removeDisconnectedMember(self, userid):
        self.members.pop(userid,None)


        


