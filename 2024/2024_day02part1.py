
fichier = open("datas/2024_day2_data","r")

lignes = fichier.readlines()

def str_to_int(tab):
    result = []
    for elt in tab:
        result.append(int(elt))
    return result

def test_safe(report):
    report = str_to_int(report)
    if report[0] > report[1]:
        in_de = "D" #decrease
    else:
        in_de = "I" #increase
    for i in range(1,len(report)):
        if in_de == "D":
            if report[i-1] <= report[i]:
                return False
            else:
                if abs(report[i-1]-report[i]) not in [1,2,3]:
                    return False
        else:
            if report[i-1] >= report[i]:
                return False
            else:
                if abs(report[i-1]-report[i]) not in [1,2,3]:
                    return False
    return True

def recherche_safe(lignes):
    safes = 0
    for i in range (len(lignes)):
        report = lignes[i].split(" ")
        if test_safe(report):
            safes += 1
    return safes

print(recherche_safe(lignes))