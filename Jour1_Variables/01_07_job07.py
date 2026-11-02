
#
#
#
# num1 = 40	Affectation d'un nombre entier à une variable.
# num2 = 2	Affectation d'un deuxième nombre entier.
# +	Opérateur d'addition pour des nombres.
# result	Variable permettant de conserver un résultat.
# print()	Affiche une valeur dans le terminal.
# f"..."	Permet d'intégrer des variables dans une chaîne de caractères.
# int	Type représentant un nombre entier.
# float	Type représentant un nombre à virgule flottante.
#
#
#


#
#
#
# Méthode 1 : — Addition mathématique.

num1 = 40
num2 = 2

print(num1 + num2)

# Résultat : 42


#
#
#
# Méthode 2 : — Concaténation

num1 = "40"
num2 = "2"

print(num1 + num2)

# Résultat : 402
#L'opérateur + possède donc plusieurs comportements selon les types de valeurs utilisés.
#C'est ce qu'on appelle la surcharge d'opérateur : un même symbole peut correspondre à différentes opérations.
#
#
#
# Méthode 3 : — Convertir du texte en nombres

num1 = "40"
num2 = "2"

result = int(num1) + int(num2)

print(result)

# Résultat : 42
# 
# 
#
#
# Méthode 3
# Une question pour vérifier ta compréhension :
# Si nous écrivons :
# 
num1 = 40
num2 = 2

result = num1 + num2

num1 = 100

result = num1 + num2

print(result)

#
# À ton avis, Python affichera 42 ou 102 ? 😏