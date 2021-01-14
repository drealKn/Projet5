import os

class Program():
    def __init__(self):
        print("""Bienvenue dans Substituts !
Vous allez pouvoir changer vos habitudes alimentaires !

Téléchargements des produits : 
                """)

    def menu(self):
        os.system('clear')
        print("1. Choisir un produit")
        print("2. Accéder aux favoris")
        print("tapez le numéro d'une catégorie ou q pour quitter")
        n = input()
        return n
        
    def category_choice(self, choices):
        os.system('clear')
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
        os.system('clear')
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
        os.system('clear')
        print("Voici les substituts")
        for substitute in substitutes:
            print(str(substitutes.index(substitute) + 1) + " - " + str(substitute))
        n = ""
        n_list = [str(substitutes.index(substitute) + 1) for substitute in substitutes]
        while n not in n_list or n.lower() == "q":
            print("Tapez le numéro d'un produit pour l'ajouter en tant que favori ou q pour quitter")
            n = input()
        return substitutes[int(n) - 1]
