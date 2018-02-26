
def checkPalindroom():

    #vraagt aantal zinnen
    aantalZinnen = int(input('Aantal zinnen: '))
    teller = 0

    #Maakt een array voor de ingevoerde zinnen
    arrZinnen = [] * aantalZinnen
    zinnenReverse = [] * aantalZinnen

    while(teller < aantalZinnen):
        zinInvoer = input('')

        #Verwijdert de spaties
        zinInvoer = zinInvoer.replace(" ", "")

        #Zet de letters naar de kleineletters
        zinInvoer = zinInvoer.lower()

        #Deze string wordt alleen met letters gevuld(nummers en tekens worden verwijderd)
        zinOnlyLetters = ''
        for letter in zinInvoer:
            #Controlleert of de element een letter is of iets an ders
            if letter.isalpha():
                #Als het letters is wordt de zinOnlyLetters gevuld
                zinOnlyLetters = zinOnlyLetters + letter

        arrZinnen.append(zinOnlyLetters)
        zinnenReverse.append(zinOnlyLetters[::-1])
        teller +=1

    for zin in arrZinnen:
        if zin == zinnenReverse[arrZinnen.index(zin)]:
            print('palindroomzin')
        else:
            print('geen palindroomzin')

if __name__ == '__main__':
    checkPalindroom()