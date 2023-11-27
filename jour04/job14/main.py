def my_long_word(number, chaine):
    mots_long = []
    mot = ""
    count = 0

    for char in chaine:
        if char != " ":
            mot += char
            count += 1
        else:
            if count > number:
                mots_long.append(mot)
            mot = ""
            count = 0

    if count > number:
        mots_long.append(mot)

    return mots_long

chiffre_entier = 3
caractere = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(chiffre_entier, caractere)
print(str(chiffre_entier) + " : " + " ".join(resultat))


