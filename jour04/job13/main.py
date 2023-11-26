def doublon(L):
    n = 0
    for i in L:
        n += 1

    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if L[i] == L[j]:
                k = j
                while k < n - 1:
                    L[k] = L[k + 1]
                    k += 1
                n -= 1
            else:
                j += 1
        i += 1

    return L[:n]

liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

resultat = doublon(liste)

print("Liste sans doublons:", resultat)





