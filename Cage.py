from Db import Db

class Cage:
    def __init__(self):
        self.table = 'cage'
        self.db = Db(host='localhost', user='root', password='root', database='zoo')

    

    def create(self,superficie, capacite):
        query = f'INSERT INTO {self.table} (superficie, capacite) VALUES ( %s, %s)'
        params = (superficie, capacite)
        self.db.executeQuery(query, params)

    def read(self):
        query = f'SELECT * FROM cage'
        return self.db.fetch(query)
    
    def update(self, superficie, capacite, id):
        query = f'UPDATE cage SET superficie=%s, capacite=%s WHERE id=%s'
        params = (superficie, capacite, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f'DELETE FROM cage WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
    
    def find(self, id):
        query = f'SELECT * FROM cage WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)
    

    def addAnimal(self, idAnimal, idCage):
        query = f'UPDATE animal SET cage_id=%s WHERE id=%s'
        params = (idCage, idAnimal)
        self.db.executeQuery(query, params)
    
    def removeAnimal(self, idAnimal):
        query = f'UPDATE animal SET cage_id=NULL WHERE id=%s'
        params = (idAnimal,)
        self.db.executeQuery(query, params)

    def getAnimals(self, idCage):
        query = f'SELECT * FROM animal WHERE cage_id=%s'
        params = (idCage,)
        return self.db.fetch(query, params)
    
    def getFreeCages(self):
        query = f'SELECT * FROM cage WHERE max_animaux > (SELECT COUNT(*) FROM animal WHERE cage_id=cage.id)'
        return self.db.fetch(query)
    
    def getFullCages(self):
        query = f'SELECT * FROM cage WHERE max_animaux <= (SELECT COUNT(*) FROM animal WHERE cage_id=cage.id)'
        return self.db.fetch(query)
    
    def getEmptyCages(self):
        query = f'SELECT * FROM cage WHERE max_animaux = 0'
        return self.db.fetch(query)
    
    def getAnimalsCount(self, idCage):
        query = f'SELECT COUNT(*) FROM animal WHERE cage_id=%s'
        params = (idCage,)
        return self.db.fetch(query, params)
    
    def getAnimalsCountByType(self, idCage, type):
        query = f'SELECT COUNT(*) FROM animal WHERE cage_id=%s AND type=%s'
        params = (idCage, type)
        return self.db.fetch(query, params)
    

