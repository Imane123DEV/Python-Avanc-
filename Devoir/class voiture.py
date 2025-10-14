class Voiture:
    def __init__(self, code, marque, puissance, kilometrage):
        self.code = code
        self.marque = marque
        self.puissance = puissance
        self.kilometrage = kilometrage
    
    def mod_puiss(self, puissance):
        self.puissance = puissance
    
    def mod_kilo(self, kilometrage):
        self.kilometrage = kilometrage
    
    def afficher(self):
        print("code:", self.code)
        print("marque:", self.marque)
        print("puissance:", self.puissance)
        print("kilometrage:", self.kilometrage)
v1=Voiture('1234','renault','90','15000')
v1.afficher()
