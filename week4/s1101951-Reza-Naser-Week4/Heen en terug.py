def decodeer(geheim, aantal):

    aantalWoorden = (len(geheim) / aantal)
    woordenInRij = []* int(aantalWoorden)
    eenWoordVanGeheim = ''
    alleWordenInEenString = ''
    gedecodeerdeZin= ''

    teller = 0
    for x in geheim:
        #Controleert of the teller kleiner is dan de aantalKolomen
        if(teller <= aantal):
            #Zo ja, word hier de string Woorden gevuld met de letter(waarde van x)
            eenWoordVanGeheim = eenWoordVanGeheim + (x)

            #De teller wordt met 1 opgehoogd
            teller +=1

            #Als de teller gelijk is aan aantalKolomen
            if teller == aantal:
                #Wordt de teller terug gezet naar 0
                teller = 0

                #De array met de baam woordenInRij word gevuld met de waardes van variabele eenWoordVanGeheim
                woordenInRij.append(eenWoordVanGeheim)

                #De waarde van de variabele eenWoordVanGeheim wordt teruggezet naar null
                eenWoordVanGeheim = ''

    for woord in woordenInRij:
        #Deze if keert de waardes om van als  % 2 == 0 een true teruggeeft
        if((woordenInRij.index(woord)+1) % 2 == 0):
            woordenInRij[woordenInRij.index(woord)] = woord[::-1]

    for woord in woordenInRij:
        #Hier word de alleWordenInEenString gevuld met alle woorden van de array > woordenInRij
        alleWordenInEenString = alleWordenInEenString + woord
    counter = 0;


    while counter < aantal:
        letterTeller = counter
        while letterTeller < len(alleWordenInEenString):
            #Hier wordt de string gedecodeerdeZin gevuld met de letter van alleWordenInEenString
            gedecodeerdeZin = gedecodeerdeZin + (alleWordenInEenString[letterTeller])

            #de variabele letterTeller wordt opgehoogd met aantalKolomen
            letterTeller += aantal
        counter += 1
    print(gedecodeerdeZin)

if __name__ == '__main__':
    gecodeerdeZin = input("Vul hier de gecodeerde zin in: ")
    aantalKolomen = int(input("Geef hier aantal kolomen: "))
    decodeer(gecodeerdeZin, aantalKolomen)