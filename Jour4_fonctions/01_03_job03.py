# 
# 🐍 Jour 4 — Job 03 : Additionner deux nombres
# 
# Créer une fonction nommée Add qui reçoit deux nombres entiers en paramètres et affiche leur somme.
# 
# 
def Add(a, b):
    resultat = a + b
    print(resultat)


Add(5, 3)
Add(10, 20)
Add(100, 250)
Add(-5, 15)
# 
# 
print (".")
print (".")
print (".")
print (".")
# 
# 🧠 Une subtilité importante : print() ou return ?
# Dans cet exercice, La Plateforme demande d'afficher la somme.
# Nous utilisons donc print().

def Add(a, b):
    return a + b


total = Add(5, 3)

print(total)
# 
# 
# 
# 
# 
# 
# 
# 