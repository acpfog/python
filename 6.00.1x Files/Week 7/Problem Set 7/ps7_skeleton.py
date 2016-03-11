import random as rand
import string
import math
import random

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        x, y = location
        self.location = ( float(x) , float(y) )
    def get_number_of_species(self, animal):
        if animal in self.species_types.keys():
            return self.species_types[animal]
        else:
            return 0
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        if species in self.species_types.keys():
            self.species_types[species] -= 1
            if self.species_types[species] < 1:
                del self.species_types[species]

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        return 1.0 * adoption_center.get_number_of_species( self.desired_species )

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.name = name
        self.desired_species = desired_species
        self.considered_species = considered_species
    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center)
        for specie in self.considered_species:
            score += 0.3 * adoption_center.get_number_of_species( specie )
        return score

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.name = name
        self.desired_species = desired_species
        self.feared_species = feared_species
    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center)
        score -= 0.3 * adoption_center.get_number_of_species( self.feared_species )
        if score < 0.0:
            score = 0.0
        return score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species
    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center)
        for specie in self.allergic_species:
            if adoption_center.get_number_of_species( specie ) > 0:
                return 0.0
        return score


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species
        self.medicine_effectiveness = medicine_effectiveness
    def get_score(self, adoption_center):
        allergic = {}
        species_types = adoption_center.get_species_count()
        for specie in species_types.keys():
            if specie in self.medicine_effectiveness.keys():
                allergic.update({ specie : self.medicine_effectiveness[specie] })
        if len(allergic.keys()) > 0:
            return sorted(allergic.values())[0] * Adopter.get_score(self, adoption_center)
        else:
            return Adopter.get_score(self, adoption_center)

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.name = name
        self.desired_species = desired_species
        self.location = location
    def get_linear_distance(self, to_location):
        x1, y1 = self.location
        x2, y2 = to_location
        return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    def get_score(self, adoption_center):
        distance = self.get_linear_distance( adoption_center.get_location() )
        if distance < 1:
            score = 1.0 * adoption_center.get_number_of_species( self.desired_species )
        elif distance < 3 and distance >= 1:
            score = random.uniform(0.7, 0.9) * adoption_center.get_number_of_species( self.desired_species )
        elif distance < 5 and distance >= 3:
            score = random.uniform(0.5, 0.7) * adoption_center.get_number_of_species( self.desired_species )
        else:
            score = random.uniform(0.1, 0.5) * adoption_center.get_number_of_species( self.desired_species )
        return score
            
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    tmp = []
    result = []
    for ac in list_of_adoption_centers:
        tmp.append( ( adopter.get_score( ac ) , ac.get_name()  , ac ) )
    for ac in sorted(tmp, key=lambda element: (-element[0], element[1])):
        result.append( ac[2] )
    return result

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    tmp = []
    result = []
    for adopter in list_of_adopters:
        tmp.append( ( adopter.get_score( adoption_center ) , adopter.get_name() , adopter ) )
    for adopter in sorted(tmp, key=lambda element: (-element[0], element[1]))[:n]:
        result.append( adopter[2] )
    return result

adopter1 = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac1 = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))


for i in get_ordered_adoption_center_list(adopter4, [ac1,ac2,ac3]):
    print i.get_name()

#print  get_ordered_adoption_center_list(adopter1, [ac1,ac2,ac3])

#for i in  get_adopters_for_advertisement(ac1, [adopter1, adopter2, adopter3, adopter4, adopter5, adopter6], 5):
#    print i.get_name()
