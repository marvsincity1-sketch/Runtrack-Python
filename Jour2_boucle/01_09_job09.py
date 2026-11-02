#  🐍 Jour 2 — Job 09 : Nombres pairs et impairs
#  
#  Créer un programme qui affiche les nombres pairs et impairs de 1 à 30, uniquement à l'aide d'une boucle.
#  
#  
for i in range(1, 31):
    print(i, "pair" if i % 2 == 0 else "impair")
#  
#  for	_____Démarre la boucle.
#  range(1, 31)	_____Parcourt les nombres de 1 à 30 inclus.
#  i % 2	_____Calcule le reste de la division de i par 2.
#  == 0	_____Vérifie si ce reste est égal à zéro.
#  if	_____Choisit le résultat lorsque la condition est vraie.
#  else	_____Choisit l'autre résultat lorsque la condition est fausse.
#  print()	_____Affiche le nombre et sa catégorie.
#  
#  