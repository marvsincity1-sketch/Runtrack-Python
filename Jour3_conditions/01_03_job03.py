#  
#  🐍 JOUR 3 — JOB 03 : Les trois nombres interdits !
#  
#  Afficher tous les nombres de 0 à 100 inclus, sauf trois :
#    26, 37 et 88.
# 
for nombre in range(101):
    if nombre != 26 and nombre != 37 and nombre != 88:
        print(nombre)
#  
#  1. for nombre in range(101):
# Nous créons une boucle qui parcourt les nombres de 0 à 100.
# Rappel : range(101) commence à 0 et s'arrête juste avant 101.
# 2. if nombre != 26
# L'opérateur != signifie « différent de ».
# Python vérifie que le nombre actuel n'est pas 26.
# 3. and
#  
#  
#  