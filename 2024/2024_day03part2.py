
import re

fichier = open("datas/2024_day3_data","r")

lignes = fichier.readlines()
for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]


def find_mul(lignes):
    somme = 0
    do_dont = 0 #do
    for ligne in lignes:
        tab = re.findall(r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)",ligne)
        for elts in tab:
            if elts[2] != '' and elts[3] != '': #mul
                if do_dont == 0:
                    fact = int(elts[2])*int(elts[3])
                    somme += fact
            if elts[1] != '': #dont
                do_dont = 1
            if elts[0] != '': #do
                do_dont = 0
    return somme
            


print(find_mul(lignes))