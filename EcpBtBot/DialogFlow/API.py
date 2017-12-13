import json

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

CLIENT_ACCESS_TOKEN = '868aec3d1e0f408392c3c2993fb05cfa'


class API:
    def __init__(self):
        #Connexion api
        self.ai=apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        
    def _get_json_response(self,user_message):
        #Sending message and getting response
        request=self.ai.text_request()
        request.query= user_message
        return json.loads(request.getresponse().read().decode())
