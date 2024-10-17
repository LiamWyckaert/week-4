#oef 14 

def geef_gemeenschappelijke_elementen (listA:list, listB:list) -> list: 
    doorsnede = []
    for element in listA:
        if element in listB and element not in doorsnede: 
            doorsnede.append(element)
    

    return doorsnede 


list1 = [78, 4, 5, 6, 4]
list2 = [89, 78, 4] 
print(f"De gemeenschappelijke elementen uit list 1 en list 2 zijn" )
print(f"\t{geef_gemeenschappelijke_elementen(list1,list2)}")

list3 = ['Tamara', 'Delfien', 'Elke', 'Marijn']
list4 = ['Natasja', 'Mieke', 'Tamara', 'Elke', 'Carine']
print(f"De gemeenschappelijke elementen uit list 3 en list 4 zijn" )
print(f"\t{geef_gemeenschappelijke_elementen(list3,list4)}")


