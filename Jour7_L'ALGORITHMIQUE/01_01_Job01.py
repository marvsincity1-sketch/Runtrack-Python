# --------------------------------------------------------
# JOB 01 — Le rectangle mystérieux !
# --------------------------------------------------------
# 
def draw_rectangle(width, height):

    for ligne in range(height):

        if ligne == 0 or ligne == height - 1:
            print("|" + "-" * (width - 2) + "|")

        else:
            print("|" + " " * (width - 2) + "|")


largeur = int(input("Quelle largeur souhaites-tu ? "))
hauteur = int(input("Quelle hauteur souhaites-tu ? "))

draw_rectangle(largeur, hauteur)
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