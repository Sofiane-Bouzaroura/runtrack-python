nom_produit="Table"
prix_unitaire= 1000.0
quantite_en_stock= 40

print("information du produit")
print("Nom:",nom_produit)
print("Prix unitaire:",prix_unitaire)
print("Quantite en stock",quantite_en_stock)

quantite_achetee=int(input("qantite voulu :"))
quantite_en_stock += quantite_achetee

prix_unitaire *= 1.1

print("\nApres l'achat et l'inflation de 10%:",prix_unitaire)
print("Nom",nom_produit)
print("Nouveau prix unitaire",prix_unitaire)
print("Nouveau quantite en stock",quantite_en_stock)