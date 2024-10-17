# oef 15
#opmerking: onderstaande oplossing kan ook via de methode set gebeuren


def verwijder_dubbels(elementen:list) -> list: 
    resultaat = []
    for element in elementen:
        #controle of het al in resultaat zit: indien niet -> toevoegen
        if element not in resultaat:
            resultaat.append(element)
    return resultaat



test = ["A", 89, 78, 4, "A", "test", 4]
print(f"{test}\nZonder dubbels: {verwijder_dubbels(test)}")


