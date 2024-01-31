from Directeur import Directeur

class Main:
    def __init__(self):
        self.directeur = Directeur()
        self.menu()

    def menu(self):
        print("1. Créer un animal")
        print("2. Lire les animaux")
        print("3. Modifier un animal")
        print("4. Supprimer un animal")
        print("5. Trouver un animal")
        print("6. Créer une cage")
        print("7. Lire les cages")
        print("8. Modifier une cage")
        print("9. Supprimer une cage")
        print("10. Trouver une cage")
        print("11. Ajouter un animal dans une cage")
        print("12. Quitter")
        choix = input("Votre choix : ")

        try:
            choix = int(choix)
        except ValueError:
            print("Choix invalide. Veuillez entrer un nombre.")
            self.menu()

        if choix == 1:
            self.createAnimal()
        elif choix == 2:
            self.readAnimal()
        elif choix == 3:
            self.updateAnimal()
        elif choix == 4:
            self.deleteAnimal()
        elif choix == 5:
            self.findAnimal()
        elif choix == 6:
            self.createCage()
        elif choix == 7:
            self.readCage()
        elif choix == 8:
            self.updateCage()
        elif choix == 9:
            self.deleteCage()
        elif choix == 10:
            self.findCage()
        elif choix == 11:
            self.addAnimalToCage()
        elif choix == 12:
            exit()
        else:
            print("Choix invalide")
            self.menu()

    def createAnimal(self):
        name = input("Nom : ")
        age = int(input("Âge : "))
        breed = input("Race : ")
        pays = input("Pays : ")
        id_cage = int(input("ID de la cage : "))

        try:
            id_cage = int(id_cage)
        except ValueError:
            print("ID de cage invalide. Veuillez entrer un nombre.")
            self.menu()

        self.directeur.createAnimal(name, age, breed ,pays ,id_cage)
        self.menu()

    def readAnimal(self):
        for animal in self.directeur.readAnimal():
            print("Animal : ")
            print(f"id : {animal[0]}")
            print(f"Nom : {animal[1]}")
            print(f"Race : {animal[2]}")
            print(f"id_cage : {animal[3]}")
            print(f"Age : {animal[4]}")
            print(f"Pays : {animal[5]}")
            print("------------------")
        self.menu()

    def updateAnimal(self):
        id_animal = input("ID de l'animal : ")
        name = input("Nom : ")
        age = input("Âge : ")
        breed = input("Race : ")

        try:
            id_animal = int(id_animal)
        except ValueError:
            print("ID d'animal invalide. Veuillez entrer un nombre.")
            self.menu()

        self.directeur.updateAnimal(id_animal, name, age, breed)
        self.menu()

    def deleteAnimal(self):
        id_animal = input("ID de l'animal : ")

        try:
            id_animal = int(id_animal)
        except ValueError:
            print("ID d'animal invalide. Veuillez entrer un nombre.")
            self.menu()

        self.directeur.deleteAnimal(id_animal)
        self.menu()

    def findAnimal(self):
        id_animal = input("ID de l'animal : ")

        try:
            id_animal = int(id_animal)
        except ValueError:
            print("ID d'animal invalide. Veuillez entrer un nombre.")
            self.menu()

        print(self.directeur.findAnimal(id_animal))
        self.menu()

    def createCage(self):
        superficie = input("Superficie de la cage : ")
        capacite = input("Nombre maximum d'animaux : ")

        try:
            superficie = int(superficie)
            capacite = int(capacite)
        except ValueError:
            print("ID de cage ou nombre maximum d'animaux invalide. Veuillez entrer un nombre.")
            self.menu()

        self.directeur.createCage(superficie, capacite)
        self.menu()

    def readCage(self):
        for cage in self.directeur.readCage():
            print("Cage : ")
            print(f"id : {cage[0]}")
            print(f"Superficie : {cage[1]}")
            print(f"Capacite : {cage[2]}")
            print("------------------")
        self.menu()

    def updateCage(self):
        id_cage = input("ID de la cage : ")
        name = input("Nom de la cage : ")
        type_cage = input("Type de la cage : ")
        max_animals = input("Nombre maximum d'animaux : ")

        try:
            id_cage = int(id_cage)
            max_animals = int(max_animals)
        except ValueError:
            print("ID de cage ou nombre maximum d'animaux invalide. Veuillez entrer un nombre.")
            self.menu()

        self.directeur.updateCage(id_cage, name, type_cage, max_animals)
        self.menu()

    def deleteCage(self):
        id_cage = input("ID de la cage : ")

        try:
            id_cage = int(id_cage)
        except ValueError:
            print("ID de cage invalide. Veuillez entrer un nombre.")
            self.menu()

        self.directeur.deleteCage(id_cage)
        self.menu()

    def findCage(self):
        id_cage = input("ID de la cage : ")

        try:
            id_cage = int(id_cage)
        except ValueError:
            print("ID de cage invalide. Veuillez entrer un nombre.")
            self.menu()

        print(self.directeur.findCage(id_cage))
        self.menu()

    def addAnimalToCage(self):
        id_animal = input("ID de l'animal : ")
        id_cage = input("ID de la cage : ")

        try:
            id_animal = int(id_animal)
            id_cage = int(id_cage)
        except ValueError:
            print("ID d'animal ou ID de cage invalide. Veuillez entrer un nombre.")
            self.menu()

        self.directeur.addAnimalToCage(id_animal, id_cage)
        self.menu()

    


Main()
