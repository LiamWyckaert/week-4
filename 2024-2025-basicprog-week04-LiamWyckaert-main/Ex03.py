#oef3
vrienden=[]

nieuweVrienden = input("Geef de naam van een vriend op, of sluit af met een leeg veld:> ")
while nieuweVrienden != "":
    vrienden.append(nieuweVrienden)
    #nieuwe vriend opvragen
    nieuweVrienden = input("Geef de naam van een vriend op, of sluit af met een leeg veld:> ")


print(f"je vrienden zijn {vrienden}")