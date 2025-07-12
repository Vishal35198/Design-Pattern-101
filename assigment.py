import uuid

class Account:
    
    def __init__(self,username,password):
        self.account_id = uuid.uuid4
        self._username = username
        self._password = password
  
  
class Device:
    def __init__(self):
        self.device_id = uuid.uuid4
        self.ip_address = None
        
    
        
#
#account.add_screen(screen1)
# accoun.add_screen(screen2) throws error cause Subscription model is 200 only
# #