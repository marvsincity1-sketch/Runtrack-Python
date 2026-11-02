#    --------------------------------------
#   🐍 Jour 4 — Job 12 : Le miroir de Python 🪞
#    --------------------------------------
#   
#   
def inverser_texte(texte):
    return texte[::-1]


print("Bienvenue dans le miroir d'Aelys !")

while True:

    texte = input("\nÉcris un mot ou une phrase : ")

    resultat = inverser_texte(texte)

    print("Texte inversé :", resultat)

    if texte.lower() == resultat.lower():
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

    continuer = input("\nContinuer ? (oui/non) : ")

    if continuer.lower() == "non":
        print("À bientôt !")
        break
    
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