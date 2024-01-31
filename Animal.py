from Db import Db

class Animal:
    def __init__(self):
        self.table = 'animal'
        self.db = Db(host='localhost', user='root', password='root', database='zoo')


    def create(self, name, age, breed, pays, id_cage):
        query = f'INSERT INTO {self.table} (nom, date_de_naissance, race, pays ,id_cage ) VALUES (%s, %s, %s, %s, %s)'
        params = (name, age, breed, pays, id_cage)
        self.db.executeQuery(query, params)

    def read(self):
        query = f'SELECT * FROM {self.table}'
        return self.db.fetch(query)

    def update(self, id, name, age, breed):
        query = f'UPDATE {self.table} SET nom=%s, date_de_naissance=%s, race=%s WHERE id=%s'
        params = (name, age, breed, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f'DELETE FROM {self.table} WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)

    def find(self, id):
        query = f'SELECT * FROM {self.table} WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)
