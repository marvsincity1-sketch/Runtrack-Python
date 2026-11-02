#  🐍 Jour 2 — Job 05 : De for à while
#  Transformer cette boucle for en boucle while pour obtenir exactement le même résultat.
#  
#   for N in range(1, 13):
#        print(N)
#

N = 1

while N <= 12:
    print(N)
    N += 1


#  N = 1	_____Initialise notre compteur à 1.
#  while	_____Lance une boucle conditionnelle.
#  N <= 12	_____Continue tant que N est inférieur ou égal à 12.
#  :	_____Annonce le bloc d'instructions.
#  print(N)	_____Affiche la valeur actuelle de N.
#  N += 1	_____Augmente N de 1 à chaque tour.
#  