
import os
from .DialogFlow.API import *
from .DialogFlow.Response import *
from .Conversational_Integration import *

print("Dire Bonjour pour commencer \n")

dico_connexions = {}

class API_reponse:

    def __init__(self, sujet):
        if sujet == "sepresenter":
            self.ai = API_SePresenter()
        elif sujet == "hotel":
            self.ai = API_Hotel()
        elif sujet == "restaurant":
            self.ai = API_Restaurant()
        elif sujet == "boulangerie":
            self.ai = API_Boulangerie()

    def reponseBot(self, message):

        user_message = message

        rep = Response(self.ai._get_json_response(user_message))

        return rep.result.fulfillment.speech
