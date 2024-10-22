# Initialiseren van variabelen
totaal_inkomsten = 0
inkomsten_type_a = 0
inkomsten_type_b = 0
inkomsten_type_c = 0
aantal_type_a = 0
aantal_type_b = 0
aantal_type_c = 0
km_type_a = 0
km_type_b = 0
km_type_c = 0

# Begin van de boekhouding
while True:
  # Invoer van de gegevens
  type_wagen = input("Geef het type wagen (A, B, C): ")
  dagen = int(input("Geef het aantal huur dagen: "))
  km = int(input("Geef het aantal gereden kilometers: "))

  # Berekening van de huurprijs
  if type_wagen == "A":
    huurprijs = 25 * dagen + 0.5 * km
    inkomsten_type_a += huurprijs
    aantal_type_a += 1
    km_type_a += km
  elif type_wagen == "B":
    huurprijs = 35 * dagen + 0.6 * km
    inkomsten_type_b += huurprijs
    aantal_type_b += 1
    km_type_b += km
  elif type_wagen == "C":
    huurprijs = 45 * dagen + 0.7 * km
    inkomsten_type_c += huurprijs
    aantal_type_c += 1
    km_type_c += km
  else:
    print("Ongeldig type wagen.")
    continue

  # Toevoegen aan de totale inkomsten
  totaal_inkomsten += huurprijs

  # Vraag aan de gebruiker om door te gaan
  doorgaan = input("Wilt u nog een wagen toevoegen? (j/n): ")
  if doorgaan.lower() != "j":
    break

# Weergave van de resultaten
print("\nOverzicht van de dag:")
print("Totale inkomsten: €", totaal_inkomsten)
print("Inkomsten van type A: €", inkomsten_type_a)
print("Inkomsten van type B: €", inkomsten_type_b)
print("Inkomsten van type C: €", inkomsten_type_c)
print("Aantal wagens type A: ", aantal_type_a)
print("Aantal wagens type B: ", aantal_type_b)
print("Aantal wagens type C: ", aantal_type_c)
print("Totaal gereden km type A: ", km_type_a)
print("Totaal gereden km type B: ", km_type_b)
print("Totaal gereden km type C: ", km_type_c)
