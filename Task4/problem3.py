class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
        
class linked:
    def __init__(self):
        self.head = None
        self.counter = 0
        
    
    def insertion(self, p, n):
        n = node(n)
        n.next = p.next
        p.next = n
        
        
    def deletion(self, d):
        store = self.head
        if store is not None:
            if (store.data == d):
                self.head = store.next
                store = None
                return
            
        while store is not None:
            if store.data == d:
                break
            
            store = store.next
            
        if(store == None):
            return
        
        
    def count(self, lst, key):    
        if not lst:  
            return self.counter
        if lst.data == key:
            
            self.counter = self.counter + 1
        return self.count(lst.next, key)