# 🐍 Jour 2 — Job 08 : Le résultat précédent + 2
# 
# Créer une boucle qui effectue 12 tours et affiche le résultat du tour précédent + 2.
# 
resultat = 0

for i in range(1, 13):
    resultat += 2
    print("Tour", i, ":", resultat)
# 
# resultat = 0	______Initialise la variable à zéro.
# for	______Démarre une boucle.
# i	______Représente le numéro du tour.
# range(1, 13)	______Effectue 12 itérations, de 1 à 12.
# resultat += 2	______Incrémente la variable resultat de 2.
# print()	______Affiche le numéro du tour et le résultat.
# 
# 