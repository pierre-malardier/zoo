from Animal import Animal
from Cage import Cage
import Db

class Directeur:

    def __init__(self) -> None:
        self.animal = Animal()
        self.cage = Cage()        
        

    def createAnimal(self, name, age, breed, pays ,id_cage):
        self.animal.create(name, age, breed, pays, id_cage)

    def readAnimal(self):
        return self.animal.read()
    
    def updateAnimal(self, id, name, age, breed):
        self.animal.update(id, name, age, breed)
    
    def deleteAnimal(self, id):
        self.animal.delete(id)
    
    def findAnimal(self, id):
        return self.animal.find(id)
    
    def createCage(self,superficie, capacite):
        self.cage.create( superficie, capacite)

    def readCage(self):
        return self.cage.read()
    
    def updateCage(self, id, name, type, maxAnimals):
        self.cage.update(id, name, type, maxAnimals)

    def deleteCage(self, id):
        self.cage.delete(id)

    def findCage(self, id):
        return self.cage.find(id)
    
    def addAnimalToCage(self, idAnimal, idCage):
        self.cage.addAnimal(idAnimal, idCage)