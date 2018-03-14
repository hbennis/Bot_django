
class DialogFlowResponse:
    """Response from DialogFlow"""
    def __init__(self, response):
        self.response=response
        self.id =  response.get('id',None)
        self.timestamp =  response.get('timestamp',None)
        self.lang =  response.get('lang',None)
    @property
    def result(self):
        return Result(self.response.get('result',None))
    @property
    def status(self):
        return Status(self.response.get('status',None))

class Result:
    def __init__(self,result):
        self.result= result
        self.source=result.get('source',None)
        self.resolvedQuery=result.get('resolvedQuery',None)
        self.parameters=result.get('parameters',None)
        self.score=result.get('score',None)
        self.contexts=result.get('contexts',None)
    @property
    def metadata(self):
        return Metadata(self.result.get('metadata',None))
    @property
    def fulfillment(self):
        return Fulfillment(self.result.get('fulfillment',None))


class Metadata:
    def __init__(self,metadata):
        self.intentName=self.intentName=metadata.get('intentName','')
            

class Fulfillment:
    def __init__(self,fulfillment):
        self.speech=fulfillment.get('speech',None)
        self.messages=fulfillment.get('messages',None)
        self.quickreplies=[]
        for quickReply in self.messages:
            if quickReply.get('type','') == 2:
                self.quickreplies=quickReply.get('replies',[])


class Status:
    def __init__(self,status):
        self.code=status.get('code',None)
        self.errorType=status.get('errorType',None)
