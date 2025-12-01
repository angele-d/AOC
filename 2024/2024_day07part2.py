import sys
sys.setrecursionlimit(10000)

fichier = open("datas/2024_day7_data","r")

lignes = fichier.readlines()

for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]


def calcul(chiffres,acc):
    if chiffres == []:
        return acc
    else:
        new_acc = []
        for i in range (len(acc)):
            new_acc.append(acc[i] * chiffres[0])
            new_acc.append(acc[i] + chiffres[0])
            new_acc.append(int(str(acc[i])+str(chiffres[0])))
        return calcul(chiffres[1:],new_acc)
            

def est_valide(ligne):
    splitter = ligne.split(": ")
    total = int(splitter[0])
    chiffres = splitter[1].split(" ")
    for i in range (len(chiffres)):
        chiffres[i] = int(chiffres[i])
    result_calculs = calcul(chiffres[1:],[chiffres[0]])
    if total in result_calculs:
        return True
    else:
        return False


def calcul_tot(lignes):
    somme = 0
    for i in range (len(lignes)):
        if est_valide(lignes[i]):
            tot = (lignes[i].split(": "))[0]
            somme += int(tot)
    return somme

print(calcul_tot(lignes))