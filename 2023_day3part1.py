
fichier = open("datas/2023_day3_data","r")

lignes = fichier.readlines()
for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]


def symboles_autour(lignes,coordonnees): #NON FINI
    '''
    :coordonnees: [[x,y],[x,y]...]
    '''
    symboles = False
    for coord in coordonnees:
        i = coord[0]
        j = coord[1]
        if j > 0:
            if lignes[i][j-1] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    symboles = True
        if j < len(lignes[0])-1:
            if lignes[i][j+1] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    symboles = True
        if i > 0:
            if lignes[i-1][j] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    symboles = True
            if j > 0:
                if lignes[i-1][j-1] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    symboles = True
            if j < len(lignes[0]) -1:
                if lignes[i-1][j+1] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    symboles = True
        if i < len(lignes)-1:
            if lignes[i+1][j] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    symboles = True
            if j > 0:
                if lignes[i+1][j-1] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    symboles = True
            if j < len(lignes[0]) -1:
                if lignes[i+1][j+1] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    symboles = True
    return symboles
            

def presence_autres_chiffres(lignes,i,j): #FAIT
    reponse = []
    while j < len(lignes[0]) and lignes[i][j] in ['0','1','2','3','4','5','6','7','8','9']:
        reponse.append([i,j])
        j += 1
    return reponse

def somme_part_numbers(lignes): #FAIT
    somme = 0
    for i in range (len(lignes)):
        j = 0
        while j < len(lignes[0]):
            if lignes[i][j] in ['0','1','2','3','4','5','6','7','8','9']:
                coord_chiffres = presence_autres_chiffres(lignes,i,j)
                if symboles_autour(lignes,coord_chiffres):
                    nombre = 0
                    decrem = len(coord_chiffres)-1
                    for coord in coord_chiffres:
                        nombre += int(lignes[coord[0]][coord[1]])*10**decrem
                        decrem -= 1
                    print(nombre)
                    somme += nombre
                j += len(coord_chiffres)
            else:
                j += 1
    return somme
    
print(somme_part_numbers(lignes))