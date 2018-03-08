
import json
import os
import sys
from .Config import *

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )



class API_Connection:
    def __init__(self,subject):
        """
        #Connexion api
        """
        CLIENT_ACCESS_TOKEN = tokens[subject]
        self.ai=apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        
    def _get_json_response(self,user_message):
        """
        #Sending message and getting response
        """
        request=self.ai.text_request()
        request.query= user_message
        return json.loads(request.getresponse().read().decode())


