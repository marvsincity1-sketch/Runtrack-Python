# -------------------------------------
# 🐍 Jour 4 — Job 05 : La calculatrice
# -------------------------------------
# Créer une fonction calcule qui reçoit trois paramètres :
#  
#  num1 : premier nombre.
#  operator : opération à effectuer (+, -, *, /, %).
#  num2 : deuxième nombre.
# 
# 
def calcule(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        return num1 / num2

    elif operator == "%":
        return num1 % num2


print(calcule(10, "+", 5))
print(calcule(10, "-", 5))
print(calcule(10, "*", 5))
print(calcule(10, "/", 5))
print(calcule(10, "%", 3))
# 
# 
# 
print (".")
print (".")
print (".")
print (".")
# 
# 
# -------------------------------------
# 🧮 Job 05 — Version 2 : La calculatrice interactive
# -------------------------------------
# 
# 
def calcule(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Erreur : division par zéro !"
        return num1 / num2

    elif operator == "%":
        if num2 == 0:
            return "Erreur : modulo par zéro !"
        return num1 % num2

    else:
        return "Opération inconnue !"


# Demander les informations à l'utilisateur

num1 = float(input("Entrez le premier nombre : "))

operator = input("Choisissez une opération (+, -, *, /, %) : ")

num2 = float(input("Entrez le deuxième nombre : "))


# Effectuer le calcul

resultat = calcule(num1, operator, num2)

print("Résultat :", resultat)
# 
# 
print (".")
print (".")
print (".")
print (".")
# 
# ------------------------------------- 
#🐍 Job 05 — Version 3 : La calculatrice en boucle !
# -------------------------------------
# 
# 
def calcule(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Erreur : division par zéro !"
        return num1 / num2

    elif operator == "%":
        if num2 == 0:
            return "Erreur : modulo par zéro !"
        return num1 % num2

    else:
        return "Opération inconnue !"


# Notre calculatrice interactive

print("Bienvenue dans la calculatrice d'Aelys !")

while True:

    num1 = float(input("Premier nombre : "))

    operator = input("Opération (+, -, *, /, %) : ")

    num2 = float(input("Deuxième nombre : "))

    resultat = calcule(num1, operator, num2)

    print("Résultat :", resultat)

    continuer = input("Voulez-vous continuer ? (oui/non) : ")

    if continuer.lower() == "non":
        print("À bientôt !")
        break


# Nous avons combiné :
#
#    def : créer une fonction réutilisable.
#    return : renvoyer le résultat d'une opération.
#    input() : récupérer les informations de l'utilisateur.
#    float() : convertir une saisie en nombre.
#    if / elif / else : sélectionner le comportement.
#    while True : répéter le programme.
#    break : interrompre la boucle.
#    .lower() : convertir du texte en minuscules.   