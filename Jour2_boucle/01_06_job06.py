#  
#  🐍 Jour 2 — Job 06 : Multiplication par 7
#  
#  Écrire un programme qui affiche, à l'aide d'une boucle while, les premiers résultats de la multiplication de N par 7.
#  
N = int(input("Entrez un nombre : "))
i = 1

while i <= N:
    print(i, "x 7 =", i * 7)
    i += 1
#  
#  input()	________Demande une valeur à l'utilisateur.
#  int()	________Convertit la saisie en entier.
#  N	________Stocke le nombre renseigné par l'utilisateur.
#  i = 1	________Initialise le compteur à 1.
#  while i <= N	________Répète la boucle tant que i est inférieur ou égal à N.
#  print()	________Affiche la multiplication et son résultat.
#  i * 7	________Multiplie le compteur par 7.
#  i += 1	________Incrémente le compteur de 1.
#  
#  