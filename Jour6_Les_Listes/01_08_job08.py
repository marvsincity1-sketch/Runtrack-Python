print(" ")
print(" ")
# ----------------------------------------------------
# 📘 JOB 08 — Calculer la somme des nombres pairs
# ----------------------------------------------------
# écrire un programme qui calcule la somme de toutes les
# valeurs paires de cette liste :
# 
# 
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme = 0

for nombre in L :
    if nombre % 2 == 0:
        somme += nombre

print(somme)
# 
# 
# 
print(" ")
print(" ")
# 
# ----------------------------------------------------
# version améliorer
# ----------------------------------------------------
# combien et qui ?
# et total de :
# 
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

compteur = 0
somme = 0

for nombre in L:
    if nombre % 2 == 0:
        compteur += 1
        somme += nombre

print("Voici une liste :")
print(L)

print("Récupération des nombres pairs et calcul de leur somme.")

print("Nombre de valeurs paires :", compteur)
print("Somme des valeurs paires :", somme)
#
#
#
print(" ")
print(" ")
# 
# 
# -------------------------------------
# Une petite amélioration des futurs programmes
# -------------------------------------
# 
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

nombres_pairs = []
compteur = 0
somme = 0

for nombre in L:
    if nombre % 2 == 0:
        nombres_pairs.append(nombre)
        compteur ++ 1
        somme += nombre

print("Liste de Départ :", L)
print("Nombres pairs trouvé", nombres_pairs)
print("Nombre de valeurs paires :", compteur)
print("Somme des valeurs paires :", somme)
# 
# 
# 
print(" ")
print(" ")
# 
# 
# 