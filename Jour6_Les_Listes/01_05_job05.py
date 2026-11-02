# ----------------------------------
# JOB 05 — Modifier une valeur avec la somme de ses voisines
# ----------------------------------
# 
# 1 Afficher la deuxième valeur de la liste.
# 2 Créer une fonction qui remplace L[3] par la somme de ses deux voisines : L[2] et L[4].
# 3 Afficher la liste modifiée, puis sa dernière valeur.
# 
L = [1, 2, 3, 4, 5]
print(L)

def modifier_liste():

    L[3] = L[2] + L[4]

modifier_liste()
print (L)
print(L[-1])
# 
# 
# 