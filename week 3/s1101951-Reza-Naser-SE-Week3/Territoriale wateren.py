import math

def berekenVoetpunt():
    x1=float(input('Invoer x1: '))
    y1= float(input('Invoer y1: '))

    x2=float(input('Invoer x2: '))
    y2=float(input('Invoer y2: '))

    x3=float(input('Invoer x3: '))
    y3=float(input('Invoer y3: '))

    #een array coordinaten met de punten
    puntenArray = [[0,12],[12,24],[24,200],[200, math.inf]]

    #een array met zone namen
    territories = ['territoriale wateren', 'aansluitende zone', 'exclusieve economische zone', 'internationale wateren']
    #berekent de voetpunt
    u = ((x3 - x1)*(x2-x1) + (y3-y1)*(y2-y1)) / ((math.pow((x2-x1), 2)) + (math.pow((y2-y1),2)))

    #berekent de x van de voetpunt
    xv = x1 + u*(x2-x1)

    # berekent de y van de voetpunt
    yv = y1 + u*(y2-y1)

    # berekent de kwadraat(afstand)
    a = math.sqrt((math.pow((xv - x3),2)) + (math.pow((yv - y3),2)))

    print('voetpunt: (' + str(xv) + ', '+ str(yv) + ') ')
    print('afstand: ' + str(a) + ' zeemijl')

    for punten in puntenArray:
        if(a > punten[0] and a < punten[1]):
            print('zone: ' + territories[puntenArray.index(punten)])
if __name__ == '__main__':
    berekenVoetpunt()