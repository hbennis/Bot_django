
import os
from .DialogFlow.API import *
from .DialogFlow.Response import *
from .Conversational_Integration import *

print("Dire Bonjour pour commencer \n")

def main():
    
    ai =API()

    while True:
        user_message= ''
        while len(user_message)==0:
            user_message=ReadingMessage()

        rep=Response(ai._get_json_response(user_message))

        try:
            _result = rep.result
            _action = rep.result.action
            _intent = rep.result.metadata.intentName
        except:
            pass
        if _intent == "AuRevoir":
            SendingMessage("Au revoir !")
            break

        actionIncomplete = rep.result.actionIncomplete
        contexts = rep.result.contexts

        if len(contexts)>0 :
            context = contexts[0]
        else:
            context=None

        SendingMessage(u"< %s" % rep.result.fulfillment.speech)


ai = API()
def reponseBot(message):


    user_message = message

    rep = Response(ai._get_json_response(user_message))

    try:
        _result = rep.result
        _action = rep.result.action
        _intent = rep.result.metadata.intentName
    except:
        pass

    #if _intent == "AuRevoir":
        #SendingMessage("Au revoir !")

    actionIncomplete = rep.result.actionIncomplete
    contexts = rep.result.contexts

    if len(contexts) > 0:
        context = contexts[0]
    else:
        context = None

    return rep.result.fulfillment.speech

