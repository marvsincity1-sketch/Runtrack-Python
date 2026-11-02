# ----------------------------------------------------
# JOB 09 — Trouver le maximum et le minimum d'une liste
# ----------------------------------------------------
# 
print(" ")
print(" ")
#
#  max() : trouver la plus grande valeur.
#  min() : trouver la plus petite valeur.
# 
# 
# Création de notre liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

maximum = max(L)

minimum = min(L)

print("Voici notre liste :", L)
print("La valeur maximale est :", maximum)
print("La valeur minimale est :", minimum)
# 
# 
# 
print(" ")
print(" ")
# 
# ------------------------------------------
#💻 Version avec une boucle for
# ------------------------------------------
#
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

maximum = L[0]
minimum = L[0]

for nombre in L:

    if nombre > maximum:
        maximum = nombre

    if nombre < minimum:
        minimum = nombre

print("Maximum :", maximum)
print("Minimum :", minimum)
# 
# 
# 
print(" ")
print(" ")
# 
# 
# 