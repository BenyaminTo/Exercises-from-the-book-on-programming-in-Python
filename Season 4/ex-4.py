import numpy as np
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',':',';','"','<','>','?','/']
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#############################################################
def encript(message):
    encrypted_message = ""
    for char in message:
        if char.upper() in letters:
            index = letters.index(char.upper())
            encrypted_message += symbols[index]  
        else:
            encrypted_message += char 
    return encrypted_message
#############################################################
def decript(message):
    decrypted_message = ""
    for char in message:
        if char in symbols:
            index = symbols.index(char)
            decrypted_message += letters[index]
        else:
            decrypted_message += char
    return decrypted_message
#############################################################
message = input("Encripting message:")
print("Encrypted message:", encript(message))
print("Decrypted message:", decript(encript(message)).title())
