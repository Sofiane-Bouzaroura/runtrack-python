def decaler_message(message="", decalage=0):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not message or decalage == 0:
        raise ValueError("")

    print(f"-> Votre message non chiffré est :\n=> {message}\n")

    message_decale = ''
    for lettre in message:
        if lettre.lower() in alphabet:
            index = (alphabet.index(lettre.lower()) + decalage) % len(alphabet)
            if lettre.isupper():
                message_decale += alphabet[index].upper()
            else:
                message_decale += alphabet[index]
        else:
            message_decale += lettre

    print(f"-> Votre message chiffré est :\n=> {message_decale}")
    return message_decale

message_original = "Ave Cesar !"
decalage = 3
resultat = decaler_message(message_original, decalage)
   




    
   




