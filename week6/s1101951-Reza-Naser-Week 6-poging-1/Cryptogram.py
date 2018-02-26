
def main():
    opgave = input("Voer de opgave in: ")
    incompleteOplossing = input("Voer hier de gedeeltelijke oplossing in: ")
    cryptogram(opgave, incompleteOplossing)

#Deze functie krijgt de opgave en gedeeltelijke oplossing als verplichte
#Argumenten mee.
def cryptogram(opgave, oplossing):
    lijstGevondenWoorden = []
    opgaveLettersInLijst = []
    oplossingLettersInLijst = []

    #Alle letters van de string oplossing worden in een lijst gezet.
    for letterInOplossing in oplossing:
        oplossingLettersInLijst.append(letterInOplossing)

        #Als de letter een alfabetische karakter is word dit in de lijst lijstGevondenWoorden toegevoegd
        #Ook wordt dezelfde index van de opgave gepakt en toegevoegd in hetzelfde object
        if letterInOplossing.isalpha():
            lijstGevondenWoorden.append([opgave[oplossing.index(letterInOplossing)], letterInOplossing])

    for letterInOpgave in opgave:
        opgaveLettersInLijst.append(letterInOpgave)

    for index in range(len(oplossingLettersInLijst)):

        #Als de letter in oplossing een vraagteken is, gaat die de lijst van gevonden worden doorzoeken.
        if oplossingLettersInLijst[index] == '?':

            #Deze forloop controlleert of de letter zich in een object van de lijst bevond
            for gevondenWoord in lijstGevondenWoorden:
                #Zo, ja dan verandert de waarde in de oplossingLettersInLijst van vraagteken naar gevonden woord.
                if opgaveLettersInLijst[index].lower() in gevondenWoord[0].lower():
                    if opgave[index].isupper():
                        oplossingLettersInLijst[index]=gevondenWoord[1].upper()
                    else:
                        oplossingLettersInLijst[index] = gevondenWoord[1].lower()
    opgaveOpgelost = ''
    for item in oplossingLettersInLijst:
        opgaveOpgelost += item
    print(opgaveOpgelost)

if __name__ == '__main__':
    main()
