# ----------------------------------------------------
#  🐍 JOB 12 — Trier une liste dans l'ordre croissant
# ----------------------------------------------------
# une fonction qui trie une liste passée en paramètre,
# sans utiliser de fonctions.
# 
# 
def trier_liste(L):

    changement = True

    while changement:

        changement = False
        precedent = 0
        premier = True

        for nombre in L:

            if premier:
                premier = False

            else:
                if L[precedent] > nombre:

                    L[precedent], L[precedent + 1] = nombre, L[precedent]

                    changement = True

                precedent += 1

    return L


L = [5, 2, 8, 1, 4]

print("Liste originale :", L)

trier_liste(L)

print("Liste triée :", L)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 