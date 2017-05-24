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
