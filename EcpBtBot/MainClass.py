
import os
import logging
from .DialogFlow.API import *
from .DialogFlow.DialogFlowResponse import *
from .Conversational_Integration import *


dico_users = {}
#dictionnaire (var globale): pour chaque clé (user), on a un dictionnaire de connexions API en fonction des thèmes

class API_reponse:

    def __init__(self, sujet):
        if sujet == "Se_presenter":
            self.ai = API_SePresenter()
        elif sujet == "Hôtel":
            self.ai = API_Hotel()
        elif sujet == "Restaurant":
            self.ai = API_Restaurant()
        elif sujet == "Boulangerie":
            self.ai = API_Boulangerie()
        elif sujet == "intro":
            self.ai = API_Intro()
        else: 
            logging.critical("Sujet non defini")

    def reponseBot(self, message):
        #user_id = user
        user_message = message
        rep = DialogFlowResponse(self.ai._get_json_response(user_message))
        
        rep_and_qr=Reponse_And_QuickReplies(rep)

        return rep_and_qr
    
class Reponse_And_QuickReplies:
    def __init__(self, reponse):
        self.speech= reponse.result.fulfillment.speech
        self.intent=reponse.result.metadata.intentName
        self.quickreplies=reponse.result.fulfillment.quickreplies
    