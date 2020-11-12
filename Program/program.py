class Program():
    def __init__(self):
        print("""Bienvenue dans Substituts !
Vous allez pouvoir changer vos habitudes alimentaires !

Téléchargements des produits : 
                """)

    def menu(self):
        print("1. Choisir un produit")
        print("2. Accéder aux favoris")
        print("tapez le numéro d'une catégorie ou q pour quitter")
        n = input()
        return n
        
    def category_choice(self, choices):
        print("Choisissez une catégorie :")        
        for category in choices:
            print(str(choices.index(category) + 1) + " - " + str(category))
        n = ""
        n_list = [str(choices.index(category) + 1) for category in choices]
        while n not in n_list or n.lower() == "q":
            print("Tapez le numéro d'une catégorie ou q pour quitter")
            n = input()        
        return choices[int(n) - 1]

    def product_choice(self, products):
        print("Choisissez un produit :")        
        for product in products:
            print(str(products.index(product) + 1) + " - " + str(product))
        n = ""
        n_list = [str(products.index(product) + 1) for product in products]
        while n not in n_list or n.lower() == "q":
            print("Tapez le numéro d'une catégorie ou q pour quitter")
            n = input()
        return products[int(n) - 1]

    def substitute_choice(self, substitutes):
        print("Voici les substituts")
        print(substitutes)
