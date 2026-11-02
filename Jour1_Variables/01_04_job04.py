# Méthode 1
print("abcdefghijklmnopqrstuvwxyz")
# print() : une fonction qui affiche une valeur.
# "abcdefghijklmnopqrstuvwxyz": une chaîne de caractères, appelée string en anglais.


# Méthode 2
alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet)
# Variable : alphabet
# Contenu : "abcdefghijklmnopqrstuvwxyz"


# Méthode 3 

import string
print(string.ascii_lowercase)

# import	Permet d'importer un module Python.
# string	Module proposant des outils et constantes pour manipuler du texte.
# .	Permet d'accéder à un élément du module.
# ascii_lowercase	Constante contenant les 26 lettres minuscules de l'alphabet anglais.
# print()	Affiche le résultat.


# Méthode 4

for lettre in "abcdefghijklmnopqrstuvwxyz":
    print(lettre)

# for  :la boucle 