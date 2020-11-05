class Program():
    def __init__(self):
        print("""Bienvenue dans Substituts !
Vous allez pouvoir changer vos habitudes alimentaires !

Téléchargements des produits : 
                """)

    def menu(self):
        print("1. Choisir un produit")
        print("2. Accéder aux favoris")
        print("tapez le numéro d'une catégorie ou q pour quitter\/n")
        n = input()
        return n
        
    def category_choice(self, choices):
        print("Choisissez une catégorie :")
        print("tapez le numéro d'une catégorie ou q pour quitter\/n")
        for category in choices:
            print(str(choices.index(category) + 1) + " - " + str(category))
        n = input()
        return n
