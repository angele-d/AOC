
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

def game_is_possible(game,nb_red,nb_green,nb_blue):
    est_possible = True
    for str in game:
        #print(str)
        if str[3:] == 'red':
            if int(str[:2]) > nb_red:
                est_possible = False
        if str[3:] == 'green':
            if int(str[:2]) > nb_green:
                est_possible = False
        if str[3:] == 'blue':
            if int(str[:2]) > nb_blue:
                est_possible = False
    return est_possible

def possible_games(games,nb_rouge,nb_vert,nb_bleu):
    somme_id = 0
    for i in range (len(games)):
        if game_is_possible(games[i],nb_rouge,nb_vert,nb_bleu):
            somme_id += i+1
    return somme_id

print(possible_games(games,12,13,14))