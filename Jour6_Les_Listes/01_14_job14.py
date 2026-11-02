# ----------------------------------------------------
# 📘 JOB 14 — Sélectionner les mots selon leur longueur
# ----------------------------------------------------
# 
# 
def my_long_word(limite, phrase):

    resultat = ""
    mot = ""
    longueur = 0

    for caractere in phrase + " ":

        if caractere != " " and caractere != ",":
            mot += caractere
            longueur += 1

        else:
            if longueur > limite:

                if resultat != "":
                    resultat += " "

                resultat += mot

            mot = ""
            longueur = 0

    return resultat


phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

print(my_long_word(3, phrase))
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