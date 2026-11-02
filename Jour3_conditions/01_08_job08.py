# 🐍 JOUR 3 — JOB 08 : Les triangles !
# 
# 
#  Si les trois longueurs permettent de construire un triangle.
#  Si le triangle est équilatéral, isocèle, rectangle ou quelconque.
#  S'il appartient à plusieurs catégories, comme un triangle rectangle et isocèle.
# 
# 
# 
a = float(input("Longueur du côté a : "))
b = float(input("Longueur du côté b : "))
c = float(input("Longueur du côté c : "))

if a <= 0 or b <= 0 or c <= 0:
    print("Les longueurs doivent être positives.")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Impossible de construire un triangle.")

else:
    print("Le triangle est valide.")

    if a == b == c:
        print("Triangle équilatéral.")

    elif a == b or a == c or b == c:
        print("Triangle isocèle.")

    else:
        print("Triangle quelconque.")

    cotes = sorted([a, b, c])

    x, y, z = cotes

    if abs(x**2 + y**2 - z**2) < 0.000001:
        print("Ce triangle est aussi rectangle.")
# 
# 
# 
# 
# 