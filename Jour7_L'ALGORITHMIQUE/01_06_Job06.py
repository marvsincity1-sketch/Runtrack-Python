# --------------------------------------------------------
#  🐍 JOUR 7-8 — JOB 06 : LES NOTES DE LUKE SKYWALKER
# --------------------------------------------------------
#   Luke note ses élèves sur 100 points.
#   l'énoncé :
#       -Les notes sont comprises entre 0 et 100.
#       -Un étudiant ayant moins de 40 échoue.
#       -Les étudiants ayant plus de 40 réussissent.
#       -L'arrondi concerne les étudiants ayant réussi.
#       -L'arrondi est effectué uniquement si la différence avec le 
#       prochain multiple de 5 est strictement inférieure à 3
#   
#   les notes aléatoires !
#   
#   
import random


def arrondir_notes(notes):

    resultat = []

    for note in notes:

        if note <= 40:
            resultat.append(note)

        else:
            reste = note % 5

            if reste >= 3:
                nouvelle_note = note + (5 - reste)
                resultat.append(nouvelle_note)

            else:
                resultat.append(note)

    return resultat


# Nombre d'élèves choisi par l'utilisateur
nombre_eleves = int(input("Combien d'élèves dans la classe ? "))

notes = []

# Génération des notes aléatoires
for i in range(nombre_eleves):

    note = random.randint(0, 100)

    notes.append(note)


# Application de notre algorithme
notes_arrondies = arrondir_notes(notes)


# Affichage des résultats
print("\n--- RÉSULTATS DE LA CLASSE ---")

for i in range(nombre_eleves):

    print(
        f"Élève {i + 1} : "
        f"{notes[i]} → {notes_arrondies[i]}"
    )
# 
# 
# 
# 
# 
# 
# 
# 
# 