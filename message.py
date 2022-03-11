class Message:
    text = str

    def __init__(self, text : str = None):
        if text is None:
            self.text = ''
        else:
            self.text = str(text)
        
    def __str__(self):
        return self.text
    
    def __len__(self):
        return len(self.text)