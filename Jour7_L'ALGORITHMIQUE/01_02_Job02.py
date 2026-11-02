# --------------------------------------------------------
# 🐍 JOUR 7-8 — JOB 02 : LE TRIANGLE
# --------------------------------------------------------
# 
# Créer un programme qui dessine un triangle à partir d'une hauteur demandée à
# l'utilisateur.
# 
def draw_triangle(height):

    for ligne in range(height):

        espaces = " " * (height - ligne - 1)

        if ligne == height - 1:
            interieur = "_" * (ligne * 2)
        else:
            interieur = " " * (ligne * 2)

        print(espaces + "/" + interieur + "\\")


hauteur = int(input("Quelle hauteur souhaites-tu ? "))

if hauteur >= 1:
    draw_triangle(hauteur)
else:
    print("La hauteur doit être au minimum de 1.")
# 
# 
# 
# 
# 
# 
# 
# 