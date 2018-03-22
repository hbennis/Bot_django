from .Member import Member
class Users_Agents(object):
    """Contains the connected members and their requested agents"""
    def __init__(self):
        self.members={}

    def connectMember(self,userid):
        if not userid in self.members:
            self.addConnectMember(userid)

    def addConnectMember(self, userid):
        member=Member(userid)
        member.user.users_bdd.connected = True
        self.members[userid] = member

    def removeDisconnectedMember(self, userid):
        self.members[userid].user.users_bdd.connected = False
        self.members.pop(userid,None)


        


