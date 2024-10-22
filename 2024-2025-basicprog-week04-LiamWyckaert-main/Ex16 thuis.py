#oef 16
#Schrijf een functie ‘geef_even_posities’ die een list als parameter binnenkrijgt. De functie maakt een
#nieuwe list aan, bestaande uit de elementen die op de even posities uit de parameter list staan.



def geef_even_posities (parlist):
    return parlist [::2]


list1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"De elementen uit {list1} op de even posities zijn: {geef_even_posities(list1)}")


