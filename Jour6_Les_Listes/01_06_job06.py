# -------------------------------------------
# JOB 06 — Échanger le premier et le dernier élément
# -------------------------------------------
# 
# Écrire un programme qui échange les valeurs de la première et de la dernière case d'une
# liste quelconque non vide.
# 
def echanger_valeurs(L):
    L[0], L[-1] = L[-1], L[0]
    return L

nombres = [1, 2, 3, 4, 5]

print (echanger_valeurs(nombres))

#
# 
#  
# 
# 
# 
# 
# 
# 