# --------------------------------------------------------
# 🐍 JOUR 7-8 — JOB 04 : LE CHIFFREMENT DE CÉSAR 🔐
# --------------------------------------------------------
# Un message à chiffrer.
# Un décalage dans l'alphabet.
# 
# 
def chiffre_cesar(message, decalage):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""

    for lettre in message.lower():

        if lettre in alphabet:

            position = alphabet.index(lettre)

            nouvelle_position = (position + decalage) % 26

            resultat += alphabet[nouvelle_position]

        else:
            resultat += lettre

    return resultat


message = input("Quel message souhaites-tu chiffrer ? ")

decalage = int(input("Quel décalage souhaites-tu ? "))

message_chiffre = chiffre_cesar(message, decalage)

print("Message original :", message)
print("Message chiffré  :", message_chiffre)
# 
# 
# 
# 
# 
# 
# 
# 