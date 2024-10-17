# oef 17
#return waarde is een list van getallen
import random

def kies_5_getallen(min: int, max: int) -> list[int]: 
    result = [] 
    for indexx in range (0,5):
        getal = random.randint(min,max)
        if getal not in result: 
            result.append(getal)
    return result




getal1 = int(input("Geef het minimum op:> "))
getal2 = int(input("Geef het maximum op:> "))
print(f"De vijf geselecteerde getallen hiertussen zijn: {kies_5_getallen(getal1, getal2)}")


