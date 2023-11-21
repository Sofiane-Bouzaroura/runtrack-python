montant_initial= 10000
taux_de_rendement_annuel= 5

gain_annuel = (taux_de_rendement_annuel / 100) * montant_initial

print("Le gain annuel initial est de:",gain_annuel)

montant_initial += 5000
taux_de_rendement_annuel += 2

nouveau_gain_annuel = (taux_de_rendement_annuel /100) * montant_initial

print("Après l'augmentation du capital et du taux de rendement, le nouveau gain annuel est de:",nouveau_gain_annuel)

retrait = 0.10 * montant_initial
montant_initial -= retrait 
taux_de_rendement_annuel -= 1
montant_final = montant_initial + nouveau_gain_annuel

print("Après le retrait , le montant final de l'investissement est de:",montant_final)



