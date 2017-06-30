# 
# You change your mind, and now want the behavior as described in problem6-1.py, except that you want:
# 
# >>> ae.say('the sky is blue')
# eric says: It is obvious that I believe that eric says: the sky is blue
# 
# >>> ae.lecture('the sky is blue')
# It is obvious that I believe that eric says: the sky is blue
#
# Change the definition of ArrogantProfessor so that the behavior described above is achieved.
#
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: ' + 'It is obvious that ' + Professor.lecture(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Professor.lecture(self, stuff)

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

print e.say('the sky is blue')
#eric says: the sky is blue
print le.say('the sky is blue')
#eric says: the sky is blue
print le.lecture('the sky is blue')
#I believe that eric says: the sky is blue
print pe.say('the sky is blue')
#eric says: I believe that eric says: the sky is blue
print pe.lecture('the sky is blue')
#I believe that eric says: the sky is blue
print ae.say('the sky is blue')
#eric says: It is obvious that I believe that eric says: the sky is blue
print ae.lecture('the sky is blue')
#It is obvious that I believe that eric says: the sky is blue

