import sys
sys.setrecursionlimit(10000)

fichier = open("datas/2024_day8_data","r")

lignes = fichier.readlines()

for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]

def transfo_str_to_tab(ligne):
    tab = []
    for carac in ligne:
        tab.append(carac)
    return tab

for i in range (len(lignes)):
    lignes[i] = transfo_str_to_tab(lignes[i])


def est_dans_tableau(coord):
    if coord[0] < 0 or coord[0] >= len(lignes):
        return False
    else:
        if coord[1] < 0 or coord[1] >= len(lignes[coord[0]]):
            return False
        else:
            return True

def antinode_key(coords_key):
    global nb_antinodes
    for i in range (len(coords_key)-1):
        for j in range (i+1,len(coords_key)):
            coord1 = coords_key[i]
            coord2 = coords_key[j]
            x_diff = coord2[0]-coord1[0]
            y_diff = coord2[1]-coord1[1]
            hash2 = (coord2[0]+x_diff,coord2[1]+y_diff)
            hash1 = (coord1[0]-x_diff,coord1[1]-y_diff)
            if est_dans_tableau(hash1) and lignes[hash1[0]][hash1[1]] != "#":
                nb_antinodes += 1
                lignes[hash1[0]][hash1[1]] = "#"
            if est_dans_tableau(hash2) and lignes[hash2[0]][hash2[1]] != "#":
                nb_antinodes += 1
                lignes[hash2[0]][hash2[1]] = "#"
            

def make_antinode(frequencies):
    liste_keys = list(frequencies)
    for key in liste_keys:
        antinode_key(frequencies[key])

def search_frequencies():
    dico = {}
    for i in range (len(lignes)):
        for j in range (len(lignes[i])):
            if lignes[i][j] not in [".","#"]:
                if dico.get(lignes[i][j]) == None: #pas encore vu
                    dico[lignes[i][j]] = [(i,j)]
                else:
                    dico[lignes[i][j]] = dico.get(lignes[i][j])+[(i,j)]
    return dico

def main():
    global nb_antinodes
    nb_antinodes = 0
    dico_frequencies = search_frequencies()
    make_antinode(dico_frequencies)

main()
print(nb_antinodes)