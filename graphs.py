class Node:
            
    def __init__(self, function = None, data = None , next : dict = None):
        if not function:
            function = self.__no_func
        self.function = function
        self.data = data
        if not next:
            next = {}
        self.next = next
        
    def __no_func(self):
        print('There is not function')



class Graph:
    
   def __init__(self, init:Node = None):
       
       if init is None:
           init = Node()
       self.current_node = init
       
   def run(self):
       ans , data = self.current_node.function(self.current_node.data)
       self.current_node.next[ans].data = data
       self.current_node = self.current_node.next[ans]

           