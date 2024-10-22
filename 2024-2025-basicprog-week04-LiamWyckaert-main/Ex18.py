# gemaakt via AI 

# Initialisatie van lijsten voor elk type werknemer
arbeiders = []
bedienden = []
kaderpersoneel = []

# Aantal werknemers in te voeren
aantal_werknemers = int(input("Geef het aantal werknemers op: > "))

# Invoer van de gegevens van elke werknemer
for i in range(aantal_werknemers):
    functie = input("Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > ").upper()
    bruto_wedde = int(input("Geef het brutowedde op: > "))

    # Toevoegen van de brutowedde aan de juiste lijst
    if functie == "A":
        arbeiders.append(bruto_wedde)
    elif functie == "B":
        bedienden.append(bruto_wedde)
    elif functie == "K":
        kaderpersoneel.append(bruto_wedde)
    else:
        print("Ongeldige functie. Probeer opnieuw.")

# Overzicht afdrukken
print("\nOverzicht:")
print("A", *arbeiders, "€")
print("B", *bedienden, "€")
print("K", *kaderpersoneel, "€")

# Totaal aantal werknemers
totaal_werknemers = len(arbeiders) + len(bedienden) + len(kaderpersoneel)

# Aantallen per type werknemer
aantal_arbeiders = len(arbeiders)
aantal_bedienden = len(bedienden)
aantal_kaderpersoneel = len(kaderpersoneel)

# Totaal brutowedde
totaal_bruto_wedde = sum(arbeiders) + sum(bedienden) + sum(kaderpersoneel)

# Afdrukken van de samenvatting
print(f"\nAantal werknemers: {totaal_werknemers}")
print(f"Aantal arbeiders: {aantal_arbeiders}")
print(f"Aantal bedienden: {aantal_bedienden}")
print(f"Aantal kaderpersoneel: {aantal_kaderpersoneel}")
print(f"Totaal brutowedde: {totaal_bruto_wedde}€")

