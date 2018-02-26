def codeer(plaintext, sleutel):
    sleutelLengte = len(sleutel)
    #Zet de letters van de sleutel om naar ASCII integers
    sleutelInIntegers = [ord(i) for i in sleutel]

    #Zet de letters van de plainText om naar ASCII integers
    plaintextInIntegers = [ord(i) for i in plaintext]

    #Dit wordt later gevuld
    versleuteldeText = ''

    for i in range(len(plaintextInIntegers)):

        #Controlleert of de index van plaintext een letter is of niet
        if plaintext[i].isalpha() and plaintext[i].isupper():
            #Zo ja, wordt de letter gecodeerd met Vigenèrecodering
            value = (plaintextInIntegers[i] + sleutelInIntegers[i % sleutelLengte]) % 26
            versleuteldeText += chr(value + 65)
        else:
            #Zo niet, wordt er niets veranderd en versleuteldeText krijgt de waarde van plaintext
            #ongewijzigd.
            versleuteldeText += plaintext[i]
    print(versleuteldeText)


def decodeer(versleuteldeText, key):
    key_length = len(key)

    # Zet de letters van de sleutel om naar ASCII integers
    sleutelNaarInt = [ord(i) for i in key]

    # Zet de letters van de plainText om naar ASCII integers
    versleuteldeTextNaarInt = [ord(i) for i in versleuteldeText]

    # Dit wordt later gevuld
    ontsleuteldeText = ''

    for i in range(len(versleuteldeTextNaarInt)):

        # Controlleert of de index van versleuteldeText een letter is of niet
        if versleuteldeText[i].isalpha() and versleuteldeText[i].isupper():
            # Zo ja, wordt de letter gedecodeerd met Vigenèrecodering
            value = (versleuteldeTextNaarInt[i] - sleutelNaarInt[i % key_length]) % 26
            ontsleuteldeText += chr(value + 65)
        else:
            # Zo niet, wordt er niets veranderd en ontsleuteldeText krijgt de waarde van versleuteldeText
            # ongewijzigd.
            ontsleuteldeText += versleuteldeText[i]

    print(ontsleuteldeText)

if __name__ == '__main__':

    decodeer('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR')
    codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR')

