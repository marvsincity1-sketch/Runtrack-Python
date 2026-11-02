#  --------------------------------------
# 🐍 Jour 4 — Job 10 : Pair ou impair ?
#  --------------------------------------
# 🎯 Consigne de La Plateforme
#   
#   Créer une fonction qui vérifie si un nombre est pair ou impair.
# 
# 
def pair_impair(nombre):

    if type(nombre) != int:
        print("Erreur : le nombre doit être un entier")

    elif nombre <= 0:
        print("Erreur : le nombre doit être positif")

    elif nombre % 2 == 0:
        print(nombre, "est pair")

    else:
        print(nombre, "est impair")


pair_impair(10)
pair_impair(13)
pair_impair(24)
pair_impair(7)
pair_impair(-5)
pair_impair(3.5)
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