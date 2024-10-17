#oef 6
klinkers = [ ] 
medeklinkers = []
woord = input("Geef een woord op:> ")
#spaties eruit gooien
woord = woord.replace(" "," ") 

for letter in woord.lower(): 
   if letter == 'a' or letter == 'i' or letter == 'o' or letter == 'e' or letter == 'u':
      if not letter in klinkers:     #dubbele eruit halen
        klinkers.append(letter)
   else: 
      if not letter in medeklinkers: #dubbels eruit halen
        medeklinkers.append(letter)

print(f"De klinkers zijn: {klinkers}")
print(f"De medeklinkers zijn: {medeklinkers}")