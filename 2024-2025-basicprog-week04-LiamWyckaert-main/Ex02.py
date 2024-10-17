#oef 2
#Maak een lege list ‘nieuwe_list_getallen’ aan.
#Vul deze list op met getallen startend vanaf 1, met stapgrootte 13, tem 482.

nieuwe_list_getallen =[]
#opvullen 
for getal in range(1,483,13): 
    nieuwe_list_getallen.append(getal)
#controle
print(nieuwe_list_getallen)
#lijst omkeren
print("lijst omgekeerd:")
nieuwe_list_getallen.reverse()
print(nieuwe_list_getallen)
#verwijder het eerste element

#nieuwe_list_getallen.pop(0)
#print(nieuwe_list_getallen)

del(nieuwe_list_getallen[0])
print(nieuwe_list_getallen)

#verwijder een specifiek element in de list
print("verwijderen van getal 300 uit de list: ")
if 301 in nieuwe_list_getallen:
    nieuwe_list_getallen.remove(301)
print(nieuwe_list_getallen)