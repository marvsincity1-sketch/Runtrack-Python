# 
# 🐍 JOUR 3 — JOB 04 : FizzBuzz !
# 
# Afficher les nombres de 1 à 100, mais avec quelques règles :
#   
#   Multiple de 3 → afficher Fizz.
#   Multiple de 5 → afficher Buzz.
#   Multiple de 3 ET de 5 → afficher FizzBuzz.
#   Sinon → afficher normalement le nombre.
# 
# 
for nombre in range(1, 101):
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    elif nombre % 3 == 0:
        print("Fizz")
    elif nombre % 5 == 0:
        print("Buzz")
    else:
        print(nombre)
# 
# 
# 
# 
# 
# 
# 