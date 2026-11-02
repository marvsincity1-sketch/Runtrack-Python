# 
# 🐍 Jour 4 — Job 02 : Les paramètres
# 
# Créer une fonction nommée My_print_name qui reçoit un paramètre name et affiche sa valeur.
# 
# 
def My_print_name(name):
    print(name)

My_print_name("Bella")
My_print_name("Aelys")
My_print_name("Lexa")
My_print_name("Robin des Bios")
# 
# 
print (".")
print (".")
print (".")
# 
# 
# 
# 💕 Petit bonus — Une fonction à deux paramètres
# 
# 
def afficher_texte(texte, mode):

    if mode == "normal":
        print(texte)

    elif mode == "inverse":
        print(texte[::-1])

    elif mode == "pyramide":
        for i in range(1, len(texte) + 1):
            print(texte[:i])


afficher_texte("Aelys", "normal")
afficher_texte("Aelys", "inverse")
afficher_texte("Aelys", "pyramide")
# 
# 
# 
# 
# 
# 
# 