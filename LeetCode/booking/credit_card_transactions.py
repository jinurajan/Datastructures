"""
"""

# Enter your code here.
"""
1.transaction -
    - auth
    - capture
2. has ttl
3. after auth hold amount
4. total amount hold < credit limit
5. take amount when capture
6. capture amount < auth amount
7. inputs
    - credit limit
    - list of credit card operations
    - id, time, operation name (AUTH / CAPTURE)
    - amount in euro
    - auth period / operation id    

things to track
1. sum of holding amount (can be changed with capture)
2. ids of auth to compare with the capture events  

- holding amount
- credit limit
- auth - {"id": (timestamp, amount, ttl)}
- usage amount

---------
Auth
---------
id , timestamp, amount, ttl, balance (timestamp + 24h) ->

balance - holded_amount


pseudo code

1. keep updating the total holding amount whenever an auth operation and return false if total hold amount > credit limit
2. keep the auth map updated 
3. when there is a capture event
    - check if there is an auth with the given id if not return False
    - if auths holding amount <= capture
    - if timestamp < auths ttl
4. return True

Assumptions
1. timestamp in integer format
2. duration is in seconds

"""
SUPPORTED_TRANSACTIONS = {"AUTH", "CAPTURE"}

class CreditTransaction:
    
    def __init__(self, limit):
        self.credit_card_limit = limit
        self.auth = {}
        self.capture = {}
        self.current_usage = 0
    
    def get_total_hold_amount(self, timestamp): 
        total_hold_amount = 0
        for id, (ts, amount, ttl, balance) in self.auth.items():
            if ttl >= timestamp:
                total_hold_amount += amount
        return total_hold_amount 
    
    def _handle_auth(self, id, timestamp, amount, duration):
        #  O(n) 
        if self.get_total_hold_amount(timestamp) + amount > self.credit_card_limit:
            return False
        ttl = timestamp + duration
        self.auth[id] = (timestamp, amount, ttl, amount)
        return True
        
    def _handle_capture(self, id, timestamp, amount, auth_id):
        # constant time
        if auth_id not in self.auth:
            return False
        auth_timestamp, auth_amount, auth_ttl, auth_balance = self.auth[auth_id]
        if auth_balance - amount < 0:
            return False
        if timestamp > auth_ttl:
            return False
        if auth_amount < amount:
            return False
        self.capture[id] = (timestamp, amount, auth_id)
        self.current_usage += amount
        self.auth[auth_id] = (auth_timestamp, auth_amount, auth_ttl, auth_balance-amount)
        return True

    def is_valid_transaction(self, id, timestamp, operation, amount, duration=None, auth_id=None):
        if operation not in SUPPORTED_TRANSACTIONS:
            return False
        # validate the duration and auth id
        if operation == "AUTH" and duration is None:
            return False
        if operation == "CAPTURE" and auth_id is None:
            return False
        
        if operation == 'AUTH':
            return self._handle_auth(id,timestamp, amount, duration)
        else:
            return self._handle_capture(id, timestamp, amount, auth_id)
        
