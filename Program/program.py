"""
This is the program module, it handles the user interface and the inputs the user enters
"""

import os
import sys
import BDD


class Program:
    def __init__(self, database):
        self.db = database
        print(
            """Bienvenue dans Substituts !
Vous allez pouvoir changer vos habitudes alimentaires !

Téléchargements des produits : 
                """
        )

    def menu(self):
        """This function handles the first menu to choose
        between the products or the saved favorites"""
        os.system("clear")
        print("1. Choisir un produit")
        print("2. Accéder aux favoris")
        n = input(
            "Entrez le numéro d'une catégorie ou q pour quitter puis appuyez sur <Entrée> :"
        )
        while n != "1" and n != "2" and n.lower() != "q":
            print("Vous n'avez pas entré une valeur valide")
            n = input(
                "Entrez le numéro d'une catégorie ou q pour quitter puis appuyez sur <Entrée> :"
            )
        if n == "1":
            category_choices = self.db.get_categories()
            category_choice = self.category_choice(category_choices)

        elif n == "2":
            favorites_choices = self.db.get_favorites()
            favorites_choice = self.favorites_choice(favorites_choices)

        elif n.lower() == "q":
            sys.exit()

    def category_choice(self, choices):
        """This function handles the menu to choose a category of products"""
        os.system("clear")
        print("Choisissez une catégorie :")
        for category in choices:
            print(str(choices.index(category) + 1) + " - " + str(category))
        n_list = [str(choices.index(category) + 1) for category in choices]
        n = input(
            "Entrez le numéro d'une catégorie ou q pour revenir au menu principal puis appuyez sur <Entrée> :"
        )
        while n not in n_list and n.lower() != "q":
            print("Vous n'avez pas entré une valeur valide")
            n = input(
                "Entrez le numéro d'une catégorie ou q pour revenir au menu principal puis appuyez sur <Entrée> :"
            )
        if n in n_list:
            category_choice = self.db.get_products(choices[int(n) - 1])
            self.product_choice(category_choice)
        elif n.lower() == "q":
            self.menu()

    def product_choice(self, products):
        """This function handles the menu to choose a products"""
        os.system("clear")
        print("Choisissez un produit :")
        for product in products:
            print(str(products.index(product) + 1) + " - " + str(product))
        n_list = [str(products.index(product) + 1) for product in products]
        n = input(
            "Entrez le numéro d'un produit ou q pour revenir au menu principal puis appuyez sur <Entrée> :"
        )
        while n not in n_list and n.lower() != "q":
            print("Vous n'avez pas entré une valeur valide")
            n = input(
                "Entrez le numéro d'un produit ou q pour revenir au menu principal puis appuyez sur <Entrée> :"
            )
        if n in n_list:
            product_choice = self.db.get_substitutes(products[int(n) - 1])
            self.substitute_choice(product_choice)
        elif n.lower() == "q":
            self.menu()

    def substitute_choice(self, substitutes):
        """This function handles the menu to add a substitute to the favorites"""
        os.system("clear")
        if substitutes:
            print("Voici les substituts :")
            for substitute in substitutes:
                print(str(substitutes.index(substitute) + 1) + " - " + str(substitute))
            n_list = [str(substitutes.index(substitute) + 1) for substitute in substitutes]
            n = input(
                "Entrez le numéro d'un produit pour l'ajouter en tant que favoris ou q pour revenir au menu principal puis appuyez sur <Entrée> :"
            )
            while n not in n_list and n.lower() != "q":
                print("Vous n'avez pas entré une valeur valide")
                n = input(
                    "Entrez le numéro d'un produit ou q pour revenir au menu principal puis appuyez sur <Entrée> :"
                )
            if n in n_list:
                self.db.add_favorite(substitutes[int(n) - 1])
                print("Le produit a été ajouté en tant que favori")
                n = input(
                    "Entrez q pour revenir au menu principal puis appuyez sur <Entrée> :"
                )
                while n != "q":
                    print("Vous n'avez pas entré une valeur valide")
                    n = input(
                        "Entrez q pour revenir au menu principal puis appuyez sur <Entrée> :"
                    )
                if n.lower() == "q":
                    self.menu()
            elif n.lower() == "q":
                self.menu()
        else:
            print("Ce produit n'a pas de substitut !")
            n = input(
                "Entrez q pour revenir au menu principal puis appuyez sur <Entrée>"
            )
            if n != "q":
                print("Vous n'avez pas entré une valeur valide")
            elif n.lower() == "q":
                self.menu()

    def favorites_choice(self, favorites):
        """This function handles the menu to look at the products saved in the favorites"""
        os.system("clear")
        if favorites != None:
            print("Voici vos favoris :")
            for favorite in favorites:
                print(str(favorites.index(favorite) + 1) + " - " + str(favorite))
                n = input(
                    "Entrez q pour revenir au menu principal puis appuyez sur <Entrée> :"
                )
            while n != "q":
                print("Vous n'avez pas entré une valeur valide")
                n = input(
                    "Entrez le numéro d'une catégorie ou q pour quitter puis appuyez sur <Entrée> :"
                )
            if n.lower() == "q":
                self.menu()
        else:
            print("Vous n'avez aucun favori")
            n = input(
                "Entrez q pour revenir au menu principal puis appuyez sur <Entrée>"
            )
            if n != "q":
                print("Vous n'avez pas entré une valeur valide")
            elif n.lower() == "q":
                self.menu()
