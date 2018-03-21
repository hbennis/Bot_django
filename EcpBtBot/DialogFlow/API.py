
import json
import logging
import os
import sys

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
    def __init__(self,subject,client_tokens):
        """
        Connexion api
        """
        if subject in client_tokens:
           CLIENT_ACCESS_TOKEN = client_tokens.get(subject,'')
        else: 
            logging.error('Subject non defined')
        
        self.ai=apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        

    def _get_json_response(self,user_message):
        """
        Sending message and getting response
        """
        request=self.ai.text_request()
        request.query= user_message
        return json.loads(request.getresponse().read().decode())


