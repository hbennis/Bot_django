import json
import sys
import os

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

CLIENT_ACCESS_TOKEN_SePresenter = '868aec3d1e0f408392c3c2993fb05cfa'


class API_SePresenter:
    def __init__(self):
        #Connexion api
        self.ai=apiai.ApiAI(CLIENT_ACCESS_TOKEN_SePresenter)
        
    def _get_json_response(self,user_message):
        #Sending message and getting response
        request=self.ai.text_request()
        request.query= user_message
        return json.loads(request.getresponse().read().decode())


CLIENT_ACCESS_TOKEN_Hotel = 'e3b0442b092c4e38a4cad3d9441d384f'


class API_Hotel:
    def __init__(self):
        # Connexion api
        self.ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN_Hotel)

    def _get_json_response(self, user_message):
        # Sending message and getting response
        request = self.ai.text_request()
        request.query = user_message
        return json.loads(request.getresponse().read().decode())


CLIENT_ACCESS_TOKEN_Restaurant = 'b4b73e19f24c441280fac1fe63297c0b'


class API_Restaurant:
    def __init__(self):
        # Connexion api
        self.ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN_Restaurant)

    def _get_json_response(self, user_message):
        # Sending message and getting response
        request = self.ai.text_request()
        request.query = user_message
        return json.loads(request.getresponse().read().decode())

CLIENT_ACCESS_TOKEN_Boulangerie = 'a690134a714c47d6b3aa45f3d470d100'


class API_Boulangerie:
    def __init__(self):
        # Connexion api
        self.ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN_Boulangerie)

    def _get_json_response(self, user_message):
        # Sending message and getting response
        request = self.ai.text_request()
        request.query = user_message
        return json.loads(request.getresponse().read().decode())