class Voiture:
    def __init__(self, code, marque, puissance, kilometrage):
        self.code = code
        self.marque = marque
        self.pauissance = puissance
        self.kilometrage = kilometrage
    
    def mod_puiss(self, p):
        self.puissance = p
    
    def mod_kilo(self, k):
        self.kilometrage = k
    
    def afficher(self):
        print("code:", self.code)
        print("marque:", self.marque)
        print("puissance:", self.puissance)
        print("kilometrage:", self.kilometrage)
        