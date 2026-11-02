# ------------------------
#   Job 03 — Ajouter un élément avec .append()
# ------------------------
#
# Écrire une fonction contenant une liste nommée fruits, composée de trois chaînes de caractères.
# Lorsque nous appelons la fonction, celle-ci doit ajouter "Melon" à la fin de la liste.
# 
def liste_fruits():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("Melon")
    print(fruits)

liste_fruits()
# 
# 
print(".")
print(".")
print(".")
print(".")
#  ------------------------
# Autre Modèle
#  ------------------------

def liste_fruits():
    fruits = ["pomme", "cerise", "orange"]

    nouveau_fruit = input("Quel fuit veut-tu ajouter ? :")

    fruits.append(nouveau_fruit)

    print(fruits)

liste_fruits()
