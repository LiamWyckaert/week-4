
#oef 10

def som_in_list (lijst_elementen): 
    som = 0 
    for getal in lijst_elementen: 
        som += getal
    return som
     
    
lijst_getallen = [5, 6, 9, 5 , 6]

print(f"De totale som is {som_in_list(lijst_getallen)}")