# oef 9

def max_en_min_uit_list(elementen):
    return str(max(elementen)) + " " + str(min(elementen))




lijst_getallen = [11, 52, 125, -89, 1245]
lijst_woorden = ["jan", "feb", "maa", "apr", "mei"]
print(f"het resultaat voor de lijst getallen is {max_en_min_uit_list(lijst_getallen)}")
print(f"het resultaat voor de lijst woorden is {max_en_min_uit_list(lijst_woorden)}")
