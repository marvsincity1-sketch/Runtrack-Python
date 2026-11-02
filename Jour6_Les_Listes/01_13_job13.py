# ----------------------------------------------------
# 📘 JOB 13 — Supprimer les doublons d'une liste
# ----------------------------------------------------
# 
# 
# 
# 
# 
def supprimer_doublons(L):

    resultat = []

    for nombre in L:

        existe = False

        for valeur in resultat:

            if nombre == valeur:
                existe = True
                break

        if existe == False:

            resultat = resultat + [nombre]

    return resultat


L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

print("Liste originale :", L)

print("Liste sans doublons :", supprimer_doublons(L))

# 
# 
# 
# 
# 