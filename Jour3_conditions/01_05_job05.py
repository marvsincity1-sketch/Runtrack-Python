# 🐍 JOUR 3 — JOB 05 : Les nombres premiers !
# 
# Créer un programme qui affiche tous les nombres premiers jusqu'à 1000.
# 
# 
for nombre in range(2, 1001):
    premier = True

    for diviseur in range(2, nombre):
        if nombre % diviseur == 0:
            premier = False
            break

    if premier:
        print(nombre)
# 
# 
# 
# 
# 
# 
# 