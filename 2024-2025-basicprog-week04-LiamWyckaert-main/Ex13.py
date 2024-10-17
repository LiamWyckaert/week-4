# oef 13

def tel_elementen_binnen_interval (elementen:list, min, max) -> int:
    aantal = 0 
   #ik overloop alle elementen
    for element in elementen:
        if element >= min and element <= max:
            aantal += 1
    return aantal


list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"Het aantal elementen dus 40 en 100 is {tel_elementen_binnen_interval(list1,40,100)}")
print(f"Het aantal elementen tussen a en e is {tel_elementen_binnen_interval(list2, "a","e")}")