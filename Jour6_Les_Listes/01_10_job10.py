# ----------------------------------------------------
# 📘 JOB 10 — Multiplier les valeurs comprises dans un intervalle
# ----------------------------------------------------
# 
print("")
print("")
# écrire un programme qui calcule le produit de toutes les valeurs 
# comprises dans l'intervalle [25, 90].
# 
# 
L=[8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]


produit = 1
# Pour afficher les nombres selectionnes
nombres_selectionnes = []

for nombre in L :
    if 25 <= nombre <= 90:
        nombres_selectionnes.append(nombre)
        produit *= nombre

print("Voici notre liste : ")
print (L)
print("")
print("Nombres sélectionnés :", nombres_selectionnes)
print("")
print ("Prduit des valeurs comprises entre 25 et 90 : ", produit)
# 
# 
# 
print("")
print("")
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