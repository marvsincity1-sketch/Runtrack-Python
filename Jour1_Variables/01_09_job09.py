#
#
# ------------------------------------------------------------
# Méthode 1 : Un affichage simple, sans présentation
# ------------------------------------------------------------

# Imaginons trois variables :
print("essai 1 ")
print(".")

product_name = "Processeur"
unit_price = 149.90
stock_quantity = 12

# Nous pourrions écrire :

print(product_name)
print(unit_price)
print(stock_quantity)

# résultat : Processeur
#            149.9
#            12
print(".")
print(".")

#########
######
###
# ------------------------------------------------------------
# Méthode 2 : Un affichage formaté avec les f-strings
# ------------------------------------------------------------
print("essai 2 ")
print(".")

product_name = "Processeur"
unit_price = 149.90
stock_quantity = 12

print(f"Produit : {product_name}")
print(f"Prix unitaire : {unit_price} €")
print(f"Quantité en stock : {stock_quantity}")

# résultat :    Produit : Processeur
#               Prix unitaire : 149.9 €
#               Quantité en stock : 12
#
#
print(".")
print(".")
#########
######
###

#
#
# Comment fonctionne le formatage ?
#
# Prenons cette ligne :

#       print(f"Produit : {product_name}")

# print()	Affiche quelque chose dans le terminal.
# f	Active le formatage de la chaîne.
# "Produit : "	Texte affiché tel quel.
# {product_name}	Remplacé par la valeur de la variable.

#
#
# ------------------------------------------------------------
# Méthode 3 Aller plus loin : contrôler des nombres
# ------------------------------------------------------------
print("essai 3 ")
print(".")
# Avant :
#           unit_price = 149.90
# Python affiche :
#            149.9
# Python conserve cette valeur sous forme de nombre et n'a pas besoin d'afficher le zéro final.


# C'est là qu'intervient :
# ⭐ Le formatage :.2f
#       print(f"Prix unitaire : {unit_price:.2f} €")

# Résultat : Prix unitaire : 149.90 €


# Décomposons :
#
#       : introduit une spécification de format.
#       .2 demande deux chiffres après le séparateur décimal.
#       f indique un format numérique à virgule flottante.


# Ce qui donne en pratique 

print(f"{unit_price:.1f}")
print(f"{unit_price:.2f}")
print(f"{unit_price:.3f}")

# Résultat :    149.9
#               149.90
#               149.900
print(".")
print(".")

#########
######
###
#
#
# ------------------------------------------------------------
# Méthode 4 : 🏆 Présenter un véritable inventaire
# ------------------------------------------------------------
print("essai 4 ")
print(".")


product_name = "Processeur"
unit_price = 149.90
stock_quantity = 12

print("================================")
print("     INVENTAIRE ROBIN DES BIOS")
print("================================")

print(f"Produit       : {product_name}")
print(f"Prix unitaire : {unit_price:.2f} €")
print(f"Stock         : {stock_quantity}")

print("================================")

print(".")
print(".")
## A voir en éxecutant le code dans le terminal !
#
#
# Notions découvertes :
#       print()	Affiche des informations dans le terminal.
#       f-string	Permet d'insérer des variables dans une chaîne de caractères.
#       {variable}	Insère la valeur d'une variable.
#       :.2f	Affiche un nombre avec deux décimales.
#       Affichage formaté	Présentation organisée et lisible des données.


# ------------------------------------------------------------
#  Exercice : 
# ------------------------------------------------------------

#avant d'attaquer ces étapes, une petite question :
#   Si nous écrivons :
print("essai 5 ")
print(".")

stock_quantity = 12

print(f"Stock disponible : {stock_quantity} unités")

print(".")
#Qu'est-ce qui apparaîtra dans ton terminal ?
#Et surtout, à ton avis, que faudrait-il modifier pour afficher :
#       Stock disponible : 12 unités
# Solution 
print(f"Stock disponible : {stock_quantity} unités")
#

print(".")
print(".")


# ------------------------------------------------------------
# Méthode 5 : Ajouter du stock
# ------------------------------------------------------------

print("essai 6 ")
print(".")
#########
######
###
#   Première méthode : ajouter une quantité fixe
#


stock_quantity = 12

stock_quantity = stock_quantity + 5

print(f"Stock disponible : {stock_quantity} unités")
#
#
print(".")
print(".")
#########
######
###
#   Deuxième méthode : demander une quantité à l'utilisateur
#
stock_quantity = 12

print(f"Stock disponible : {stock_quantity} unités")

added_quantity = int(input("Combien d'unités ajouter au stock ? "))

stock_quantity += added_quantity

print(f"Nouveau stock : {stock_quantity} unités")

#   input()	Demande à l'utilisateur de saisir quelque chose au clavier.
#   "Combien d'unités..."	Message affiché dans le terminal.
#   int()	Transforme le texte saisi en nombre entier.
#   added_quantity	Variable qui conserve la quantité saisie.
#   +=	Ajoute cette quantité à la valeur existante.
#
print(".")
print(".")
#
# ------------------------------------------------------------
# Méthode 6 : Ajouter du stock
# ------------------------------------------------------------
#   🛒 Étape 1 — Le client achète des produits
#------------------------------------------------------------
#
product_name = "Processeur"
unit_price = 149.90
stock_quantity = 20
# Maintenant, le client arrive et souhaite acheter quelques processeurs.
purchase_quantity = int(input("Combien d'unités souhaitez-vous acheter ? "))

stock_quantity -= purchase_quantity

print(f"Stock restant : {stock_quantity} unités")
# purchase signifie « achat ».
# quantity signifie « quantité ».
# purchase_quantity conserve donc la quantité achetée.
#
#------------------------------------------------------------
#📈 Étape 2 — L'inflation de 10 %
#------------------------------------------------------------
# Maintenant, La Plateforme demande d'augmenter le prix du produit de 10 %.
#------------------------------------------------------------
unit_price = 149.90
increase = unit_price * 0.10
unit_price = unit_price + increase
#
#1 représente 100 % du prix initial.
# 0.10 représente les 10 % supplémentaires.
# 1.10 représente donc 110 % du prix initial.
#
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
#------------------------------------------------------------
#🏆 Étape 3 — Notre programme complet
#------------------------------------------------------------
# ============================================================
# JOB 09 — GESTION D'UN INVENTAIRE
# ============================================================

# 1. Création du produit
product_name = "Processeur"
unit_price = 149.90
stock_quantity = 12

# 2. Affichage initial
print("===== INVENTAIRE INITIAL =====")
print(f"Produit : {product_name}")
print(f"Prix unitaire : {unit_price:.2f} €")
print(f"Stock disponible : {stock_quantity} unités")

# 3. Ajout de produits
stock_quantity += 8

print("\n===== APRÈS LIVRAISON =====")
print(f"Stock disponible : {stock_quantity} unités")

# 4. Achat par un client
purchase_quantity = int(input("\nCombien d'unités souhaitez-vous acheter ? "))

stock_quantity -= purchase_quantity

# 5. Inflation de 10 %
unit_price *= 1.10

# 6. Affichage final
print("\n===== INVENTAIRE ACTUALISÉ =====")
print(f"Produit : {product_name}")
print(f"Prix unitaire : {unit_price:.2f} €")
print(f"Stock disponible : {stock_quantity} unités")
#
#
#
#
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
#
#
# ============================================================
# JOB 09 — GESTION D'UN INVENTAIRE
# ===========================================================
#               Améliorer
#------------------------------------------------------------
#
#
# JOB 09 — Gestion d'un inventaire

# 1. Création du produit
product_name = "Processeur"
unit_price = 149.90
stock_quantity = 12

# 2. Affichage initial
print("===== INVENTAIRE INITIAL =====")
print(f"Produit : {product_name}")
print(f"Prix unitaire : {unit_price:.2f} €")
print(f"Stock disponible : {stock_quantity} unités")

# 3. Ajout de produits au stock
stock_quantity += 8

print("\n===== APRÈS LIVRAISON =====")
print(f"Stock disponible : {stock_quantity} unités")

# 4. Achat par un client
purchase_quantity = int(input("\nCombien d'unités souhaitez-vous acheter ? "))

stock_quantity -= purchase_quantity

# 5. Augmentation du prix de 10 %
unit_price *= 1.10

# 6. Affichage final
print("\n===== INVENTAIRE ACTUALISÉ =====")
print(f"Produit : {product_name}")
print(f"Prix unitaire : {unit_price:.2f} €")
print(f"Stock disponible : {stock_quantity} unités")
#
#
#
#
#
#
#
#