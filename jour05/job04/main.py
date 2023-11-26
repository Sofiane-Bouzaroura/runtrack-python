def colonne_diagonale(n):
    angle= "+"
    for i in range(n + 1): angle += "-"
    angle+= "+"

    print(angle)
    for i in range(n + 1):
        tapis= ""
        for j in range(n - i): tapis+= "#"
        tapis+= " "
        for j in range(i): tapis+= "#"
        print("|" + tapis + "|")
       
    print(angle) 
	  
colonne_diagonale(10)	  
  
