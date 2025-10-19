class Employe:
    def __init__(self,Identifiant, Nom , Prenom, DateNaissance, DateEmbauche, Salaire):
        self.Identifiant = Identifiant
        self.Nom = Nom
        self.Prenom = Prenom
        self.DateNaissance = DateNaissance
        self.DateEmbaiche = DateEmbauche
        self.Salaire = Salaire
    def afficher(self):
        print(f"Identifiant : {self.Identifiant}")
        print(f"Nom : {self.Nom}")
        print(f"Prenom : {self.Prenom}")
        print(f"Date de Naissance : {self.DateNaissance}")
        print(f"Date d'emabuche : {self.DateDembauche}")
        print(f"Salaire : {self.Salaire}")
    def initialiser(self, Nom, Prenom, DateNaissance, DateEmbauche, Salaire ):
        
