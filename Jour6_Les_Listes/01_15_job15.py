# ----------------------------------------------------
#  📘 JOB 15 — Arrondir et trier sans fonctions système
# ----------------------------------------------------
# 
# 
def arrondir_et_trier(L):

    resultat = []

    # Première étape : arrondir les nombres
    for nombre in L:

        entier = nombre // 1

        decimal = nombre - entier

        if decimal >= 0.5:
            entier += 1

        resultat = resultat + [entier]

    # Deuxième étape : trier les nombres
    changement = True

    while changement:

        changement = False
        i = 0

        for nombre in resultat:

            if i > 0:

                if resultat[i - 1] > resultat[i]:

                    resultat[i - 1], resultat[i] = resultat[i], resultat[i - 1]

                    changement = True

            i += 1

    return resultat


L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

print("Liste originale :", L)

print("Liste arrondie et triée :", arrondir_et_trier(L))
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
# 
# 
# 
# 
# 
# 