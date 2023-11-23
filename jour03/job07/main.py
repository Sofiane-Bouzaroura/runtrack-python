def ton_avenir(langage):
    if langage == "javaScript":
        print ("Tu es un développeur web")
    elif langage == "python":
        print ("Tu es un développeur IA")
    elif langage == "java":
        print ("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print ("Tu es un développeur mobile")    
    else:
        print ("Un jour, je serai le meilleur développeur")
        
langage_user = input("Entrez votre langage de programmation : ")
ton_avenir(langage_user)
        