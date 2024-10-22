def zijn_gelijk(list1, list2):
 
  list1.sort()
  list2.sort()

  for element in list1:
    if element not in list2:
      return False
  for element in list2:
    if element not in list1:
      return False
  return True


lijst1 = [1, 2, 3, 4, 5]
lijst2 = [5, 4, 3, 2, 1]
lijst3 = [1, 2, 3, 4]

print(f"Lijst 1 en 2 zijn gelijk: {zijn_gelijk(lijst1, lijst2)}")  
print(f"Lijst 1 en 3 zijn gelijk: {zijn_gelijk(lijst1, lijst3)}")  

# het resultaat dat je krijgt is een bool, het is ofwel 0(false) of 1 (true) 