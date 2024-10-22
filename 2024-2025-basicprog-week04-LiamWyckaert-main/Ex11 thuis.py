#oef 11

def gemiddelde_in_list (getallen): 
    som = 0
    aantal = 0
    for getal in getallen:
        som += getal
        aantal += 1
    gemiddelde = som / aantal
    gemiddelde = round(gemiddelde,2)
    return gemiddelde



lijst_getallen = [12, 45, 465, 78, 1, 23, 89]
lege_lijst_getallen = []

print(f"Het gemiddelde is {gemiddelde_in_list(lijst_getallen)}")

