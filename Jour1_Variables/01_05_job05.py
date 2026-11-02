###
###
###
###

#Méthode 1 — Écrire directement l'alphabet inversé

print("zyxwvutsrqponmlkjihgfedcba")


###
###
###
###

#Méthode 2 — Utiliser une variable et le slicing

alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[::-1])

# [::-1] s'appelle un slicing (découpage de séquence).

# Sa structure générale est : sequence[debut:fin:pas]

#debut	Position à partir de laquelle commencer
#fin	Position où s'arrêter (exclue)
#pas	Nombre de positions parcourues à chaque déplacement
#-1	Parcourir la séquence en sens inverse


#Avec d'autre chaîne de carrectères
mot = "Robin"

print(mot[::-1])

###
###
###
###

# Méthode 3 — Utiliser reversed()
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("".join(reversed(alphabet)))

#Ici, nous découvrons deux nouveaux outils :
#reversed() parcourt les caractères dans l'ordre inverse.
#join() rassemble les caractères pour reconstruire une chaîne.
#Les guillemets vides "" indiquent qu'on ne souhaite placer aucun séparateur entre les lettres.

###
###
###
###

# Méthode 4 — Utiliser une boucle for

alphabet = "abcdefghijklmnopqrstuvwxyz"

for lettre in reversed(alphabet):
    print(lettre, end="")

#Cette méthode permet de découvrir une boucle.
#La boucle for parcourt les lettres une par une.
#L'argument end="" indique à print() de ne pas ajouter de retour à la ligne après chaque caractère.
#Ainsi, les lettres apparaissent toutes sur une seule ligne.