
fichier = open('datas/2023_day2_data','r')

lignes = fichier.readlines()
for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]
    sans_game = lignes[i].split(": ")
    lignes[i] = sans_game[1]

games = []
for i in range(len(lignes)):
    sets = lignes[i].replace("; ",", ")
    games.append(sets.split(", "))

fichier.close()

def separation_couleurs(game):
    '''
    Separation en tab [rouge,vert,bleu] de (int)
    '''
    red = []
    green = []
    blue = []
    for i in range (len(game)):
        de = game[i].split(" ")
        if de[1] == "red":
            red.append(int(de[0]))
        if de[1] == "green":
            green.append(int(de[0]))
        if de[1] == "blue":
            blue.append(int(de[0]))
    return [red,green,blue]

def puissance_1_game(game):
    sep_couleurs = separation_couleurs(game)
    result_couleurs = []
    for couleur in sep_couleurs:
        max = 0
        for nb in couleur:
            if nb > max:
                max = nb
        result_couleurs.append(max)
    puissance = result_couleurs[0] * result_couleurs[1] * result_couleurs[2]
    return puissance
        
def somme_puissances_ens_min(games):
    somme = 0
    for i in range (len(games)):
        somme += puissance_1_game(games[i])
    return somme

print(somme_puissances_ens_min(games))