#
#
#
# Méthode 1

ma_string = "Je suis une String"

print(ma_string)

# ma_string	Nom de la variable.
# =	Opérateur d'affectation.
# "Je suis une String"	Valeur stockée dans la variable.
# "	Guillemets délimitant une chaîne de caractères.

age = 43

#signifie que la variable age reçoit le nombre entier 43.


#
#
#
# Méthode 2
# La formatrice recommande d'écrire les noms de variables en anglais.

my_string = "Je suis une String"

print(my_string)

#
#
#
# Méthode 3

my_string = "Je suis une String"

print(f"Voici ma variable : {my_string}")

# f indique une chaîne formatée.
# Les guillemets délimitent le texte.
# {my_string} indique à Python d'insérer la valeur de la variable.
# print() affiche le résultat.


#
#
#
# Méthode 3 : bonus : examiner le type d'une variable
my_string = "Je suis une String"

print(my_string)
print(type(my_string))

# Nouvelle découverte : type() !
# Cette fonction permet de connaître le type d'une valeur.
# Ici, Python nous répond str, abréviation de string.#

# Résultat :    Je suis une String
#               <class 'str'>

#
#
#
# Une autre méthode

my_number = 42

print(type(my_number))

# Résultat : <class 'int'>


