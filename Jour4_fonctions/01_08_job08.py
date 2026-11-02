# --------------------------------------
# 🐍 Jour 4 — Job 08 : Le marchand des quatre saisons 🍎🥕
# --------------------------------------
# 
# 
# Créer une fonction qui reçoit deux paramètres :
#     
#     type : "fruits" ou "légume".
#     saison : "hiver" ou "été".
# 
def aliments(type, saison):

    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")

    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")

    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")

    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")

    else:
        print("Aucun résultat pour cette combinaison")


aliments("fruits", "hiver")
aliments("fruits", "été")
aliments("légume", "hiver")
aliments("légume", "été")
# 
# 
# 
print (".")
print (".")
print (".")
print (".")
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