
import re

fichier = open("datas/2024_day3_data","r")

lignes = fichier.readlines()
for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]


def find_mul(ligne):
    somme = 0
    tab = re.findall(r'mul\((\d+),(\d+)\)',ligne)
    for tuple in tab:
        fact = int(tuple[0])*int(tuple[1])
        somme += fact
    return somme
            

def init(lignes):
    somme = 0
    for i in range (len(lignes)):
        somme += find_mul(lignes[i])
    return somme

print(init(lignes))