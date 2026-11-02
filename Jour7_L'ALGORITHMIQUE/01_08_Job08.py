# --------------------------------------------------------
#  🐍 JOUR 7-8 — JOB 08 : LE GRAND TRI ! ⚔️
# --------------------------------------------------------
#    créer une fonction appelée my_sort() qui :
#           Reçoit une liste de nombres.
#           Compare les éléments voisins.
#           Échange leurs positions lorsqu'ils ne sont pas dans l'ordre.
#           Répète les opérations jusqu'à ce que la liste soit triée.
#           Compte et affiche le nombre total d'échanges effectués
#           Retourne la liste triée.
#           
import random


def my_sort(nombres):

    coups = 0
    changement = True

    # Répéter tant qu'un échange a eu lieu
    while changement:

        changement = False

        # Comparer les éléments voisins
        for i in range(len(nombres) - 1):

            if nombres[i] > nombres[i + 1]:

                # Échanger les deux éléments
                nombres[i], nombres[i + 1] = nombres[i + 1], nombres[i]

                # Compter chaque échange
                coups += 1

                changement = True

    print("Nombre total de coups :", coups)

    return nombres


# Demander combien de nombres générer
quantite = int(input("Combien de nombres souhaites-tu trier ? "))

nombres = []

# Générer une liste aléatoire
for i in range(quantite):

    nombres.append(random.randint(0, 100))


print("\nListe originale :", nombres)

# Trier notre liste
liste_triee = my_sort(nombres.copy())

print("Liste triée :", liste_triee)
# 
# 
# 
# 
# 
# 
# 