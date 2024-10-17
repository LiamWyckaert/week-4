# Feedback week 3
# Find the errors - zoek de fouten
# Make the code work for upper and lower case - zorg dat de code werkt voor hoofdletters en kleine letters

# #EN
# def count_vowels(parsentence:str) -> int:
#     number_vowels = 0
#     for letter in parsentence:
#         if letter = 'a' or letter = 'i' or letter = 'o' and letter = 'e' or letter = 'u':
#             number_vowels =+ 1
#         else:
#             number_vowels = 0
#         return number_vowels

# sentence = input("Enter a sentence:> ")
# number = count_vowels(sentence)
# print(f"The number of vowels in the sentence is: {number}")


# #NL
def tel_aantal_klinkers(parzin:str) -> int:
    aantal_klinkers = 0
    for letter in parzin:
         if letter == 'a' or letter == 'i' or letter == 'o' or letter == 'e' or letter == 'u':
             aantal_klinkers += 1
             #correctie: return stond in de for lus, daarom keerde hij na de 1Ste lus al terug
    return aantal_klinkers

zin = input("Geef een zin op:> ")
aantal = tel_aantal_klinkers(zin)
print(f"Het aantal klinkers in de zin is: {aantal}")