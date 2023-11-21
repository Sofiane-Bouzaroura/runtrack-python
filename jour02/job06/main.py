# for n in range (1,1000):
#     if n > 1:
#         for i in range(2,n):
#             if n

# def est_premier(nomber):
#     if nomber < 2:
#         return False

# for i in range(2, int(nomber**0.5) + 1):
#     if (nomber % i == 0):    
#         return False
            
# return True

# def afficher_nombres_premiers(maximum):
#     for nomber in range(2, maximum + 1):
#          if est_premier(nomber):
#               print(nomber, end=' ')
#               afficher_nombres_premiers(1000)

def est_premier(nombre):
    if nombre < 2:
        return False

    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False

    return True

def afficher_nombres_premiers(maximum):
    for nombre in range(2, maximum + 1):
        if est_premier(nombre):
            print(nombre, end=' ')

afficher_nombres_premiers(1000)
