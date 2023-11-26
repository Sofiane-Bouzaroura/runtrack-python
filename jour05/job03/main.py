def triangle(height):
    for i in range(1, height + 1):
        n = ' ' * (height - i)
        if i == height:
            print(n + '_' * (2 * i - 1))
        else:
            print(n + '/' + ' ' * (2 * (i - 1)) + '\\')

hauteur = int(input("Entrez la hauteur du triangle : "))

triangle(hauteur)



