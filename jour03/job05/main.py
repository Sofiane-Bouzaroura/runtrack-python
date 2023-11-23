def calcule(num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Opérateur non valide"


num1 = input("Entrez le premier nombre : ")
operator = input("Entrez l'opérateur (+, -, *, /, %) : ")
num2 = input("Entrez le deuxième nombre : ")


resultat = calcule(num1, operator, num2)
print("Résultat :", resultat)
