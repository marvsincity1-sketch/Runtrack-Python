# --------------------------------------------------------
# 🐍 JOUR 7-8 — JOB 03 : LE TAPIS DIAGONAL
# --------------------------------------------------------
# 
# une fonction qui reçoit une taille n en paramètre et affiche un tapis traversé par
# une diagonale.
# 
# 
def draw_carpet(n):

    # Bordure supérieure
    print("+" + "-" * (n + 1) + "+")

    # Construction des lignes du tapis
    for ligne in range(n + 1):

        # Position de la diagonale
        position = n - ligne

        # Construction de la ligne
        interieur = ""

        for colonne in range(n + 1):

            if colonne == position:
                interieur += " "
            else:
                interieur += "#"

        # Affichage de la ligne terminée
        print("|" + interieur + "|")

    # Bordure inférieure
    print("+" + "-" * (n + 1) + "+")


# L'utilisateur choisit la taille
taille = int(input("Quelle taille souhaites-tu pour ton tapis ? "))

if taille >= 0:
    draw_carpet(taille)
else:
    print("Erreur : la taille ne peut pas être négative.")
# 
# 
# 
# 
# 
# 
# 