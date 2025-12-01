
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

def recherche(tab,elt):
    nb_occurence = 0
    for element in tab:
        if element == elt:
            nb_occurence += 1
    return nb_occurence

def similarities(tabgauche,tabdroite):
    somme = 0
    for elt in tabgauche:
        nb_occurence = recherche(tabdroite,elt)
        fact = elt * nb_occurence
        somme += fact
    return somme

print(similarities(tabgauche,tabdroite))