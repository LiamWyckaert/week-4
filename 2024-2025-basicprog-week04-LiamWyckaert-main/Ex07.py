# oef 7 

def geef_info_list(naam_list:str, list_elementen:list) -> str: 
    resultaat = f"verzameling {naam_list}\n"
    positie = 0
    for element in list_elementen:  
        #opmerking: index geeft de positie van het 1ste voorkomen van het element terug
        #resultaat = resultaat + f" {element} op positie {list_elementen.index(element)}\n" 
        # oplossing: hou zelf de positie bij (vergeet ni de positie up te daten) 
        resultaat = resultaat + f" {element} op positie {positie}\n
        positie += 1 
    return resultaat







collection1 = [12, 45, -9, -15]
collection2 = [12.23, 45.1, 9.478, 15.125, -3.14]
collection3 = ["Joerie", "Marie", "Henk", "Stijn"]

print(geef_info_list("gehele getallen", collection1))
print(geef_info_list("kommagetallen" ,collection2))
print(geef_info_list("vrienden " ,collection3))