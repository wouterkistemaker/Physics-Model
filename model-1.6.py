# Dit model beschrijft de beweging van een bolvormig object
# dat met een te bepalen beginsnelheid naar beneden valt in
# een zwembad (lees: een bak water)

# In de comments worden een aantal afkortingen gebruikt, waarvan
# hier een overzicht is:
# m = meter
# kg = kilogram
# l = liter
# n = newton
# s = seconde
# h = hoogte (hiervoor wordt als referentiepunt de ONDERKANT van de bal gerekend)

# Lees a^b als a tot de macht b
# In de code zie je dat terug met a**b
# bijvoorbeeld straal**3 betekent straal tot de macht 3

# s.e. staat voor self-explanatory (vereist geen verdere uitleg)

import math

# Constanten
pi = 3.14159265359                                                                                  # wiskundige constante
g = 9.81                                                                                            # valversnelling
weerstandscoëfficient = 0.47                                                                        # "" van de basketbol
waterdiepte = 0.2                                                                                   # m, s.e.
werphoogte = 5                                                                                      # hoogte vanaf de grond vanwaar de basketbol wordt gegooid
dt = 0.001                                                                                          # s, s.e.
nulpuntDecimalen = 4                                                                                # Alles dat op 4 decimalen afgerond 0.0000 is, wordt beschouwd als het nulpunt
nulpunt = 0.001

dichtheidWater = 997                                                                                # kg/m^3, s.e.
dichtheidLucht = 1.293                                                                              # kg/m^3, s.e.

# Overige variabelen (startwaarden)                                                                 
beginsnelheid = 0                                                                                   # m/s
tijd = 0                                                                                            # s
snelheid = beginsnelheid                                                                            # m/s
hoogte = waterdiepte + werphoogte                                                                   # m

# Basketbol gegevens
massa = float(input("Vul de massa van de bol in: "))                                                # kg, heeft hier geen waarde maar wordt bepaalt zodra ik het programma opstart en ik de massa invul.
diameter = 0.216                                                                                    # m
omtrek = pi * diameter                                                                          # m                                                                              
straal = diameter / 2                                                                               # m

volume = (4/3) * pi * straal**3                                                                     # m^3
volumeInLiters = 1000 * volume                                                                      # l

frontaalOpp = pi * straal**2                                                                        # m^2

# Tegenwerkende krachten
archimedeskracht = g * dichtheidWater * volume                                                      # n
waterweerstand = 0.5 * frontaalOpp * weerstandscoëfficient * dichtheidWater * snelheid**2           # n
luchtweerstand = 0.5 * frontaalOpp * weerstandscoëfficient * dichtheidLucht * snelheid**2           # n

# Voorwaartse kracht
zwaartekracht = massa * g                                                                           # n                                                    

# Model Logica

def calculateVolume(h):                                                                             # functie die het volume van een boldeel berekend bij een gegeven hoogte
    straalBolschijf = calculateRadius(h)
    return ((pi * h)/6) * (3*(straal**2) + h**2)

def calculateRadius(h):                                                                             # hulp-functie voor de straal van de bolkap 
    try:
        return math.sqrt(straal**2 - (straal-h)**2)
    except:
        print("Negative square root! -> " + str((straal**2 - (straal-h)**2)))                       # Dit except deel was omdat ik eerst een error had dat ik een wortel van een negatief getal
        print("r-squared = %f , r-h-squared = %f" % (straal**2, (straal-h)**2))                     # probeerde te nemen, wat uiteraard niet met reeële getallen kan...

laatsteSnelheid = 0

while (hoogte > 0):
    tijd = tijd + dt;

    if (hoogte < waterdiepte):
        # de bol is nu in het water
        boldeelOnderwater  = waterdiepte - hoogte # slechte benaming, maar dit het deel van de verticale straal van de bol dat zich onder het wateroppvlak bevindt

        if (boldeelOnderwater < diameter):
            boldeelVolume = calculateVolume(boldeelOnderwater) # volume van het deel van de bol dat onder water is
            archimedeskracht = g * dichtheidWater * boldeelVolume
        else:
            # de bol is volledig onder water
            archimedeskracht = g * dichtheidWater * volumeInLiters

        waterweerstand = 0.5 * frontaalOpp * weerstandscoëfficient * dichtheidWater * snelheid**2
        nettokracht = zwaartekracht - archimedeskracht - waterweerstand
    else:
        # bol is nog boven water
        luchtweerstand = 0.5 * frontaalOpp * weerstandscoëfficient * dichtheidWater * snelheid**2
        nettokracht = zwaartekracht - luchtweerstand
        
    versnelling = nettokracht/massa

    laatsteSnelheid=snelheid;
    snelheid = snelheid + versnelling*dt;
    hoogte = hoogte - snelheid*dt;

    if (snelheid<0 ):
        if (hoogte <= nulpunt):
            print("De bol heeft de bodem bereikt.")
        else:
            print("Onder deze omstandigheden gaat de bol de bodem niet halen!")
        break;
    
    print("T= %.04f - V= %.04f - A= %0.4f - H= %.04f" % (tijd, snelheid, versnelling, hoogte))

if (hoogte < 0):
    print("De bol heeft de bodem bereikt. H=%.04f" % (hoogte))
else:
    print("De bol gaat de bodem zo niet halen!")

    
print("M= %f - D= %f" % (massa, waterdiepte))
print("Dichtheid = %0.4f" % (massa/volume))
