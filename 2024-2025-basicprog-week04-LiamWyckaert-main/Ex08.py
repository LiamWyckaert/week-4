#oef 8
import random

#deze functie kiest een element uit een doorgegeven list
def kies_element(list_elementen): 
    #kies en geef terug
    return random.choice(list_elementen)





maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober","november", "decemeber"]
getallen = [100, 200, 300, 400]

print(f"de gekozen maand is {kies_element(maanden)}")
print(f"het gekozen getal is {kies_element(getallen)}")