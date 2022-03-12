
class Node:
            
    def __init__(self, function = None, data = None , next : dict = None):
        self.function = function
        self.data = data
        if not next:
            next = {}
        self.next = next
        
    def __call__(self, *args, **kwargs):
        if self.function:
            ans , data = self.function(*args, **kwargs)
            return ans , data
        else:
            return None
        
    def __str__(self):
        return 'Holi'
        



class Graph:
    
   def __init__(self, init:Node = None):
       
       if not init:
           init = Node()
       self.current_node = init
       self.history = []

   def run(self):
       ans , data = self.current_node(self.current_node.data)
       self.current_node.next[ans].data = data
       self.current_node = self.current_node.next[ans]
       
     