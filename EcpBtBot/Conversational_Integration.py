from EcpBtBot.MainClass import *

def Receiving_Response(message,userid):
    #initialisation du sujet
    if "subject" not in dico_users[userid]:
        dico_users[userid]["subject"] ="intro"

    subject = dico_users[userid]["subject"] 

    if subject not in dico_users[userid]:
        dico_users[userid][subject] = API_Response(subject)
        #si l'utilisateur n'a jamais choisi ce thème, ouvrir une connexion API correspondante
    connexion = dico_users[userid][subject]
    repBot = connexion.ResponseBot(message)
    intent = repBot.intent
        
    if intent in tokens:
        dico_users[userid]["subject"] = intent
    if intent.upper() == "AU REVOIR":
        dico_users[userid]["subject"] = "intro"
    return repBot