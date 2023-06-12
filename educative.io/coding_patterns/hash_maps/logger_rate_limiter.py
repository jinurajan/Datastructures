"""
Logger Rate Limiter

For the given stream of message requests and their timestamps as input, you must implement a logger rate limiter system that decides whether the current message request is displayed. The decision depends on whether the same message has already been displayed in the last 
S seconds. If yes, then the decision is FALSE, as this message is considered a duplicate. Otherwise, the decision is TRUE.


"""


class RequestLogger:

    def __init__(self, time_limit):
        self.requests = {}
        self.limit = time_limit
    

    # This function decides whether the message request should be accepted or rejected
    def message_request_decision(self, timestamp, request):
        if request not in self.requests or timestamp-self.requests[request] >= self.limit:
            self.requests[request] = timestamp
            return True
        else:
            return False
        
