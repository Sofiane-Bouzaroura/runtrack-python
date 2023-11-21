alphabet="ABCDEGHIJKLMNOPQRSTUVWXYZ" *10
for n in range(len(alphabet)):
    if n % 2 != 0:
        print(alphabet[:n])