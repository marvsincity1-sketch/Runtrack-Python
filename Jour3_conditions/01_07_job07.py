# 🐍 JOUR 3 — JOB 07 : La pyramide alphabétique !
# 
# À partir de l'alphabet répété 10 fois, créer une pyramide dont chaque ligne contient davantage de caractères que la précédente.
# 
# 
alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

position = 0
longueur = 1

while position + longueur <= len(alphabet):
    print(alphabet[position:position + longueur])
    position += longueur
    longueur += 1
# 
# 
# 
# 
# 
# 
# 