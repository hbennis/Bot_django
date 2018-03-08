
import logging
import os
from .Conversational_Integration import *
from .DialogFlow.API import *
from .DialogFlow.DialogFlowResponse import *
from .DialogFlow.Config import *



dico_users = {}
"""
dictionnaire (var globale): pour chaque clé (user), on a un dictionnaire de connexions API en fonction des thèmes
"""

class API_Response(object):

    def __init__(self, subject):

        
        if subject in tokens:
            self.ai = API_Connection(subject)
        else: 
            logging.critical("Subject non defined")

    def ResponseBot(self, message):
        rep = DialogFlowResponse(self.ai._get_json_response(message))
        rep_and_qr=Response_And_QuickReplies(rep)
        return rep_and_qr
    
class Response_And_QuickReplies:
    def __init__(self, Response):
        self.speech = Response.result.fulfillment.speech
        self.intent = Response.result.metadata.intentName
        self.quickreplies = Response.result.fulfillment.quickreplies
    
