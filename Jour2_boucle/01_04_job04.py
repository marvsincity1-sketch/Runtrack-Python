#  🐍 Jour 2 — Job 04 : Les tables de multiplication
#  
#  Créer un programme qui affiche les tables de multiplication de 1 à N.
#  
#
n = int(input("Entrez un nombre supérieur à 0 : "))

for i in range(1, n + 1):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
# 
#  input()	_____Demande à l'utilisateur de saisir une valeur.
#  int()	_____Convertit la valeur saisie en nombre entier.
#  n	_____Contient le nombre choisi par l'utilisateur.
#  for i in range(1, n + 1)	_____Parcourt les tables de 1 jusqu'à N inclus.
#  for j in range(1, 11)	_____Parcourt les multiplicateurs de 1 à 10.
#  i * j	_____Calcule la multiplication.
#  print()	_____Affiche l'opération et son résultat.
#
#  
#  
#  
#  
#  
#  
#  