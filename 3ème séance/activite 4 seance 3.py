class Personne:
    def __init__(self, nom, adresse):
        self.nom=nom
        self.adresse=adresse
    def afficher(self):
        print(f"nom : {self.nom}")
        print(f"adresse : {self.adresse}")
class Employe(Personne):
    def __init__(self, nom, adresse, cnss):
        self.cnss=cnss
        Personne.__init__(self, nom, cnss)
    def afficher(self):
            Personne.afficher(self)
            print(f"cnss : {self.cnss} ")
class Enseignant(Personne):
    def __init__(self, nom, adresse, cnops):
            self.cnops=cnops
            Personne.__init__(self, nom, cnops)
    def afficher(self):
            Personne.afficher(self)
            print(f"cnops : {self.cnops} ")
class Etudiant(Personne):
    def __init__(self, nom, adresse, cne):
            self.cne=cne
            Personne.__init__(self, nom, cne)
    def afficher(self):
            Personne.afficher(self)
            print(f"cne : {self.cne} ")
p1=Personne("aymane","agadir")
p1.afficher()
em1=Employe("ali","rabat","12345")
em1.afficher()
#pour afficher seulement 2 instances pour employe (polymorphisme)
Personne.afficher(em1)
ens1=Enseignant("aymane","agadir","67890")
ens1.afficher()
et1=Etudiant("youssef","casablanca","54321")
et1.afficher()


             
   