"""
This is the program module, it handles the user interface and the inputs the user enters
"""

import os
import sys
import BDD


class Program:
    """This is the program class it handles all the functions for the ui"""
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
        print("3. Effacer la base de données")
        n = input(
            "Entrez le numéro d'une catégorie ou q pour quitter puis appuyez sur <Entrée> :"
        )
        while n != "1" and n != "2" and n != "3" and n.lower() != "q":
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
        elif n == "3":
            self.delete_database()

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
        """This function handles the menu to choose a substitute"""
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
                data = self.db.get_product_data(substitutes[int(n) - 1])
                self.product_data(data, substitutes)
            elif n.lower() == "q":
                self.menu()
        else:
            print("Ce produit n'a pas de substitut !")
            n = input(
                "Entrez q pour revenir au menu principal puis appuyez sur <Entrée> :"
            )
            if n != "q":
                print("Vous n'avez pas entré une valeur valide")
            elif n.lower() == "q":
                self.menu()

    def product_data(self, data, substitutes):
        """This module handles the menu to show the data of a substitute and adding it to the favorites"""
        os.system("clear")
        print("Voici les informations sur ce substitut :")
        print(data[0])
        print("Nutriscore : " + data[1])
        print("Ce produit peut être acheté chez : " + data[2])
        print("Page du produit : " + data[3])
        print("""Pour ajouter ce produit en favori, entrez a
Pour revenir au choix des substituts, entrez b
Pour revenir au menu principal, entrez q""")
        n = input("Entrez votre choix puis appuyez sur <Entrée> pour valider :")
        while n.lower() != "a" and n.lower() != "b" and n.lower() != "q":
            print("Vous n'avez pas entré une valeur valide")
            n = input("Entrez votre choix puis appuyez sur <Entrée> pour valider :")
        if n.lower() == "a":
            self.db.add_favorite(data[0])
            self.substitute_choice(substitutes)
        elif n.lower() == "b":
            self.substitute_choice(substitutes)
        elif n.lower() == "q":
            self.menu()


    def favorites_choice(self, favorites):
        """This function handles the menu to look at the products saved in the favorites"""
        os.system("clear")
        if favorites != None:
            print("Voici vos favoris :")
            for favorite in favorites:
                print(str(favorites.index(favorite) + 1) + " - " + str(favorite))
            n_list = [str(favorites.index(favorite) + 1) for favorite in favorites]
            n = input(
                "Entrez le numéro d'un produit ou q pour revenir au menu principal puis appuyez sur <Entrée> :"
            )
            while n not in n_list and n.lower() != "q":
                print("Vous n'avez pas entré une valeur valide")
                n = input(
                    "Entrez le numéro d'un produit ou q pour revenir au menu principal puis appuyez sur <Entrée> :"
                )
            if n in n_list:
                data = self.db.get_product_data(favorites[int(n) - 1])
                self.favorite_data(data, favorites)
            elif n.lower() == "q":
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

    def favorite_data(self, data, favorites):
        """This module handles the menu to show the data of a substitute and adding it to the favorites"""
        os.system("clear")
        print("Voici les informations sur ce favori :")
        print(data[0])
        print("Nutriscore : " + data[1])
        print("Ce produit peut être acheté chez : " + data[2])
        print("Page du produit : " + data[3])
        print("Pour revenir au menu principal, entrez q")
        n = input("Entrez votre choix puis appuyez sur <Entrée> pour valider :")
        while n.lower() != "q":
            print("Vous n'avez pas entré une valeur valide")
            n = input("Entrez votre choix puis appuyez sur <Entrée> pour valider :")
        if n.lower() == "q":
            self.menu()

    def delete_database(self):
        """This function handles the menu to delete the database"""
        os.system("clear")
        print("Êtes-vous sur de vouloir faire cela ?")
        print("1. Oui")
        print("2. Non")
        n = input("Entrez 1 ou 2 puis valider avec <Entrée>")
        while n != "1" and n != "2":
                print("Vous n'avez pas entré une valeur valide")
                n = input("Entrez 1 ou 2 puis valider avec <Entrée> :")
        if n == "1":
            self.db.delete_database()
            sys.exit()
        elif n == "2":
            self.menu()
