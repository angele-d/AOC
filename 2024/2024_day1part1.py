
fichier = open("datas/2024_day1_data","r")

lignes = fichier.readlines()

tabgauche = []
tabdroite = []
for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]
    parsing = lignes[i].split("   ")
    lignes[i] = parsing
    tabgauche.append(int(lignes[i][0]))
    tabdroite.append(int(lignes[i][1]))

def tri(tab):
    for i in range (len(tab)):
        min = i
        for j in range (i,len(tab)):
            if tab[min] > tab[j]:
                min = j
        temp = tab[min]
        tab[min] = tab[i]
        tab[i] = temp
    return tab

def calcul(tabgauche,tabdroite):
    trigauche = tri(tabgauche)
    tridroite = tri(tabdroite)
    somme = 0
    for i in range (len(tridroite)):
        diff = abs(trigauche[i]-tridroite[i])
        somme += diff
    return somme

print(calcul(tabgauche,tabdroite))