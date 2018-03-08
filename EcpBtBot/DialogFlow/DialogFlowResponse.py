class DialogFlowResponse:
    """description of class"""
    def __init__(self, response):
        """Constructeur de notre classe"""
        self.response=response
        self.id =  response['id']
        self.timestamp =  response['timestamp']
        self.lang =  response['lang']
    @property
    def result(self):
        return Result(self.response['result'])
    @property
    def status(self):
        return Status(self.response['status'])

class Result:
    def __init__(self,result):
        self.result= result
        self.source=result['source']
        self.resolvedQuery=result['resolvedQuery']
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
        self.intentName=""
        if 'intentName' in metadata.keys():
            self.intentName=metadata['intentName']
class Fulfillment:
    def __init__(self,fulfillment):
        self.speech=fulfillment['speech']
        self.messages=fulfillment['messages']
        self.quickreplies=[]
        for QuickReply in self.messages:
            if QuickReply['type']==2:
                self.quickreplies=QuickReply['replies']
class Status:
    def __init__(self,status):
        self.code=status['code']
        self.errorType=status['errorType']
