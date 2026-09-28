class Produit:
    def __init__(self,nom,prix,stock):
        self.nom=nom
        self.prix=prix
        self.stock=stock
    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prix : {self.prix:,} Ar")
        print(f"Stock : {self.stock}")
        print("Informations du produit :")
        print(f"Valeur du stock : {self.prix * self.stock:,} Ar")
    def afficher_supplementaire(self):
        print("Ce produit est frais")
    def afficher_nom(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Stock : {self.stock}")
        print("Modification faite directement sur GitHub")
        print("Test de git fetch")
        print("Modification distante")
