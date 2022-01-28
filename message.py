class Message:
    text = str
    encryption = bool
    def __init__(self, text : str, encryption : bool = False):
        
        self.text = text
        self.encryption = encryption




