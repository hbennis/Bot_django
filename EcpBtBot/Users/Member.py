from EcpBtBot.MainClass import API_Response

class Member(object):
    def __init__(self,userid):
        
        self.connectedAgents={}
        self.subject='intro'
        self.connectedAgents['intro'] = API_Response('intro')
        
    def connectToAgent(self, subject):
        #subject = subject == '' gérer le cas au revoir/intent
        self.connectedAgents[subject] = API_Response(subject)

    def checkConnection(self, subject):
        if not subject in self.connectedAgents:
            self.connectToAgent(subject)

    def disconnectAgent(self, subject):
         self.connectedAgents.pop(subject,None)