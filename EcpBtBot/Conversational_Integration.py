from .Users.Users_Agents import Users_Agents
from EcpBtBot.MainClass import API_Response

users_agents=Users_Agents()

def Receiving_Response(message,userid):
    """
    Send the response(speech and quick replies) of the bot for a given user
    """
    users_agents.connectMember(userid)

    subject = users_agents.members.get(userid).subject
    users_agents.members.get(userid).checkConnection(subject)
    connexion = users_agents.members.get(userid).connectedAgents.get(subject)
    
    client_tokens = connexion.client_tokens
    repBot = connexion.responseBot(message)
    intent = repBot.intent

    if intent in client_tokens:
        users_agents.members.get(userid).subject = intent

    if intent.upper() == 'AU REVOIR':
        users_agents.members.get(userid).disconnectAgent(subject)
        users_agents.members.get(userid).subject = 'intro'

    return repBot