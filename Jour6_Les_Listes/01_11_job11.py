# ----------------------------------------------------
#  📘 JOB 11 — Incrémenter chaque élément d'une liste
# ----------------------------------------------------
# 
# 
print(" ")
print(" ")
# 
# 
# 
L = [7, 11, 42, 39, 2]

print("Liste initiale :", L)

for i in range(len(L)):
    L[i] += 1

print("Liste modifiée :", L)
# 
# 
# 
print(" ")
print(" ")
# 
# 
# 
# 
#   len() retourne le nombre d'éléments.
#   range() permet de parcourir une séquence d'entiers.
#   L[i] permet d'accéder à un élément précis.
#   += 1 permet d'incrémenter une valeur.
#   Modifier L[i] modifie directement la liste.
# 
# 
# 
L = [2, 4, 6, 8, 10]

for i in range(len(L)):
    L[i] += i

print(L)
# 
# 
# 