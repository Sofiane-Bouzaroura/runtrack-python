def le_bon_nombre(nombre):
    if nombre > 0:
        resultat = "positif"
    elif nombre < 0:
        resultat = "negatif"
    else:
        resultat = "nul"

    print(f"Le nombre {nombre} est {resultat}.")

nombre = float(input("Veuillez entrer un nombre : "))

le_bon_nombre(nombre)

