max=1000
for nomber in range(2,max +1):
    est_premier=True

    if nomber < 2:
        est_premier=False

    for n in range(2, int(nomber**0.5) +1):
        if nomber % n == 0:
            est_premier = False
            break
    if est_premier:
        print(nomber, end=" ")        