# --------------------------------------
# 🐍 Jour 4 — Job 09 : Le bulletin scolaire 📚
# --------------------------------------
# 
# 🎯 Consigne de La Plateforme
#      
#      Créer une fonction nommée moyenne qui reçoit trois notes et retourne leur moyenne.
#      
#      Ensuite, demander trois notes à l'utilisateur, enregistrer le résultat dans une variable moyenne_etudiant, puis afficher une appréciation.
# 
# 
# 
def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3


# Demander les trois notes

note1 = float(input("Première note : "))
note2 = float(input("Deuxième note : "))
note3 = float(input("Troisième note : "))


# Calculer la moyenne

moyenne_etudiant = moyenne(note1, note2, note3)

print("Votre moyenne est :", round(moyenne_etudiant, 2))


# Déterminer l'appréciation

if moyenne_etudiant >= 15:
    print("Très bon élève")

elif moyenne_etudiant >= 11:
    print("Bon élève")

elif moyenne_etudiant >= 8:
    print("Élève moyen")

else:
    print("Élève devant faire des efforts")
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