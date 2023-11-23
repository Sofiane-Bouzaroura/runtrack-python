def tout_saison(type, saison):
    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruits" and saison == "ete":
        return "Poire, fraise, cassis"
    elif type == "legume" and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type == "legume" and saison == "ete":
        return "artichaut, aubergine, navet"
    else:
        return "Aucune correspondance trouvée."

type = input("Entrez fruits ou legume : ")
saison = input("Entrez la saison : ")

resultat = tout_saison(type, saison)
print(resultat)



