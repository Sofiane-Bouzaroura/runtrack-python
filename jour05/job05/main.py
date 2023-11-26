# def uncaesarize_letter(letter):
#     if 'A' <= letter.upper() <= 'Z':
#         return chr(ord(letter) - 3)
#     else:
#         return letter

# def caesarize_letter(letter):
#     if 'A' <= letter.upper() <= 'Z':
#         return chr(ord(letter)  3)
#     else:
#         return letter

# def caesarize(text):
#     return ''.join([caesarize_letter(letter) for letter in text])

# def uncaesarize(text):
#     return ''.join([uncaesarize_letter(letter) for letter in text])

# print(caesarize('AOUCOU JULIE'))

def cesar_lettre(lettre):
    if 'A' <= lettre.upper() <= 'Z':
        start = ord('a') if lettre.islower() else ord('A')
        return chr((ord(lettre) - start + 3) % 26 + start)
    else:
        return lettre

def lecesar_lettre(lettre):
    if 'A' <= lettre.upper() <= 'Z':
        start = ord('a') if lettre.islower() else ord('A')
        return chr((ord(lettre) - start - 3) % 26 + start)
    else:
        return lettre

def cesar(text):
    return ''.join([cesar_lettre(lettre) for lettre in text])

def lecesar(text):
    return ''.join([lecesar_lettre(lettre) for lettre in text])

print(cesar('Message chiffrer de cesar'))
