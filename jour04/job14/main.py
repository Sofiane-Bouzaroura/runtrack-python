# def my_long_word():
#     mots = ()
#     mots_long = [caractere for caractere in chiffre_entier if chiffre_entier > caractere]
#     return mots_long

# chiffre_entier = 4
# caractere = ("Bienvenue dans le monde de la programmation avec Python")
# resultat = my_long_word(chiffre_entier , caractere)

# print(resultat)

# def chaine(L):
#     n = (L)
#     i = 0
#     while i < n:
#         j = i + 4
#         while j < n:
#             if L[i:i+4] == L[j:j+4]:
#                 k = j
#                 while k < n - 4:
#                     L[k:k+4] = L[k+4:k+8]
#                     k += 4
#                 n -= 4
#             else:
#                 j += 4
#         i += 4
#     return L[:n]

# liste = list("Bienvenue dans le monde de la programmation avec Python")

# resultat = chaine(liste)
# print(resultat)








def my_long_word(number, chaine):
    mots_long = []
    mot = ""
    count = +1

    for char in chaine:
        if char != " ":
            mot += char
            count += 1
        else:
            if count > number:
                mots_long.append(mot)
            mot = ""
            count = +1

    if count > number:
        mots_long.append(mot)

    return mots_long

chiffre_entier = 4
caractere = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(chiffre_entier, caractere)
print(chiffre_entier + resultat)


