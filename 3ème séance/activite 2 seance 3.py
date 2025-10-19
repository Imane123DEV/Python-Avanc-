class Etudiant:
    def __init__(self, matricule, nom, prenom, note):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.note = note
    def afficher(self):
        print(f"matricule : {self.matricule}")
        print(f"nom : {self.nom}")
        print(f"prenom : {self.prenom}")
        print(f"note : {self.note}")
    def somme(self, autre_etudiant):
        print(f"la somme des est : {self.note + autre_etudiant.note}")
    def moyenne(self, autre_etudiant):
        print(f"la moyenne est : {(self.note + autre_etudiant.note)/2}")
e1=Etudiant('123','salma', 'said', 15)
e2=Etudiant('124', 'imane', 'ait', 18)
e1.afficher()
e2.afficher()
e1.somme(e2)
e1.moyenne(e2)
