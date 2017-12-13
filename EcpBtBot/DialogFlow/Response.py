class Response:
    """description of class"""
    def __init__(self, response):
        """Constructeur de notre classe"""
        self.response=response
        self.id =  response['id']
        self.timestamp =  response['timestamp']
        self.lang =  response['lang']

        #self.result =  Result(response['result'])
        #self.alternateResult =  response.get('alternateResult'
    @property
    def result(self):
        return Result(self.response['result'])
    @property
    def status(self):
        return Status(self.response['status'])

class Result:
    def __init__(self,result):
        self.result= result
        self.action=result['action']
        self.source=result['source']
        self.resolvedQuery=result['resolvedQuery']
        self.actionIncomplete=result['actionIncomplete']
        self.parameters=result['parameters']
        self.score=result['score']
        self.contexts=result['contexts']
    @property
    def metadata(self):
        return Metadata(self.result['metadata'])
    @property
    def fulfillment(self):
        return Fulfillment(self.result['fulfillment'])

class Metadata:
    def __init__(self,metadata):
        self.intentId=metadata['intentId']
        self.webhookUsed=metadata['webhookUsed']
        self.webhookForSlotFillingUsed=metadata['webhookForSlotFillingUsed']
        self.intentName=metadata['intentName']
class Fulfillment:
    def __init__(self,fulfillment):
        self.speech=fulfillment['speech']
        self.messages=fulfillment['messages']
class Status:
    def __init__(self,status):
        self.code=status['code']
        self.errorType=status['errorType']

