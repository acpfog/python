# 
# In your Queue class, you will need three methods:
# 
# __init__: initialize your Queue (think: how will you store the queue's elements? You'll need to initialize an appropriate object attribute in this method)
# insert: inserts one element in your Queue
# remove: removes (or 'pops') one element from your Queue and returns it. If the queue is empty, raises a ValueError.
# 

class Queue(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        self.vals.append(e)
    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError

q1 = Queue()
q2 = Queue()
q1.insert(17)
q2.insert(20)
q1.remove()
q2.remove()
