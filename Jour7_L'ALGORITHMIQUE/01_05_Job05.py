# --------------------------------------------------------
# 🐍 JOUR 7-8 — JOB 05 : LE GARDIEN DE PHARE 🚽
# --------------------------------------------------------
# Notre pauvre gardien de phare descend aux toilettes 5 fois par jour.
# Petit problème : les toilettes sont au rez-de-chaussée, et lui travaille tout en haut du phare !
# 
# 
def distance_gardien(marches, hauteur_cm):

    # Calcul de la hauteur totale en centimètres
    hauteur_totale = marches * hauteur_cm

    # Conversion des centimètres en mètres
    hauteur_m = hauteur_totale / 100

    # Une descente et une remontée
    aller_retour = hauteur_m * 2

    # Cinq passages aux toilettes par jour
    distance_jour = aller_retour * 5

    # Sept jours dans une semaine
    distance_semaine = distance_jour * 7

    print(
        f"Pour {marches} marches de {hauteur_cm} cm, "
        f"le gardien parcourt {distance_semaine:.2f} m par semaine."
    )


# Saisie des dimensions
marches = int(input("Combien de marches comporte le phare ? "))

hauteur = float(input("Quelle est la hauteur d'une marche en cm ? "))

# Vérification des valeurs
if marches > 0 and hauteur > 0:
    distance_gardien(marches, hauteur)
else:
    print("Erreur : les valeurs doivent être strictement positives.")
# 
# 
# 
# 
# 
# 
# 
# 