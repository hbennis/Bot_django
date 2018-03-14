
import logging
import os
from .Conversational_Integration import *
from .DialogFlow.API import API_Connection
from .DialogFlow.DialogFlowResponse import DialogFlowResponse

class API_Response(object):
    """ Handles the connexion to the agents """
    def __init__(self, subject):
        #TODO: Add a function to import client tokens from an extenal db 
        #(Bonus: control this db with an admin access)
        self.client_tokens={
            "Hôtel":'e3b0442b092c4e38a4cad3d9441d384f',
            "Se_presenter":'868aec3d1e0f408392c3c2993fb05cfa',
            "Restaurant":'b4b73e19f24c441280fac1fe63297c0b',
            "Boulangerie":'a690134a714c47d6b3aa45f3d470d100',
            "intro":'2037ebf0bdb4466fb5c675a8afcec15a'
        }
        self.ai = API_Connection(subject,self.client_tokens)

    def responseBot(self, message):
        rep = DialogFlowResponse(self.ai._get_json_response(message))
        rep_and_qr=Response_And_QuickReplies(rep)
        return rep_and_qr
    

class Response_And_QuickReplies:
    def __init__(self, Response):
        self.speech = Response.result.fulfillment.speech
        self.intent = Response.result.metadata.intentName
        self.quickreplies = Response.result.fulfillment.quickreplies
    