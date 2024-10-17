#oef12

#deze funtie geeft trui terug als er gemeenschappelijke elementen zijn
#false is het andere geval
def zijn_totaal_verschillend (parlist1:list, parlist2:list): 
    for element in parlist1:
        if element in parlist2:
            #bingo: element zit ook in list 2
            return False  
    return True


list_getallen1 = [4, 5, 6, 4]
list_getallen2 = [89, 78, 4]
print(f"zijn deze lists totaal verschillend? {zijn_totaal_verschillend(list_getallen1, list_getallen2)}")


