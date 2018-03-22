from EcpBtBot.MainClass import API_Response
from django.contrib.auth.models import User
from bot.models import Discussion, Users_bdd

class Member(object):
    def __init__(self,userid):

        self.user = User.objects.get(id=userid)
        self.connectedAgents={}
        self.subject=self.user.users_bdd.current_subject
        self.connectedAgents[self.subject] = API_Response(self.subject)
        
    def connectToAgent(self, subject):
        #subject = subject == '' gérer le cas au revoir/intent
        self.connectedAgents[subject] = API_Response(subject)

    def checkConnection(self, subject):
        if not subject in self.connectedAgents:
            self.connectToAgent(subject)

    def disconnectAgent(self, subject):
         self.connectedAgents.pop(subject,None)