# ----------------------------------------------
# 🐍 JOB 07 — Comprendre la logique
# ----------------------------------------------
# 
# 
print (" ")
print (" ")
# Première Idée légèrment ajouster par GPT:
# 
# 1 Prendre une liste de nombres. ✅
# 2 Faire parcourir cette liste par une boucle for. ✅
# 3 Utiliser une condition if pour tester chaque nombre. ✅
# 4 Récupérer uniquement les nombres divisibles par 3. ✅
# 
#  ce qui est presque bon !
# 
#  Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste :
#  L = [8, 24, 48, 2, 16]
# 
L =[8, 24, 48, 2, 16]

compteur = 0

for nombre in L:
    if nombre % 3 == 0:
        compteur += 1

print(compteur)
# 
# 
# 
# 
print (" ")
print (" ")
# 
# ----------------------------------------------
#  Première Idée :
# ----------------------------------------------
# 
#  Retourné des nombres divisibles par 3
#  ce qui n'est pas l'intitulé de base !! ^^
#
L = [8, 24, 48, 2, 16]

multiples =[]

for nombre in L:
    if nombre % 3 == 0:
        multiples.append(nombre)

print(multiples)
# 
# 
# 
# 
print (" ")
print (" ")
# 
# 