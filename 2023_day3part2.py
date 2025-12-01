
fichier = open("datas/2023_day3_data","r")

lignes = fichier.readlines()
for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]


def chiffres_autour(lignes,coord):
    '''
    :coord: coord d'une *
    :return: coords des chiffres
    '''
    chiffres = []
    i = coord[0]
    j = coord[1]
    if i > 0:
        if j > 0:
            if lignes[i-1][j-1] in ['0','1','2','3','4','5','6','7','8','9']:
                chiffres.append([i-1,j-1])
        if lignes[i-1][j] in ['0','1','2','3','4','5','6','7','8','9']:
                chiffres.append([i-1,j])
        if j < len(lignes[0]) -1:
            if lignes[i-1][j+1] in ['0','1','2','3','4','5','6','7','8','9']:
                chiffres.append([i-1,j+1])
    if j > 0:
        if lignes[i][j-1] in ['0','1','2','3','4','5','6','7','8','9']:
                chiffres.append([i,j-1])
    if j < len(lignes[0])-1:
        if lignes[i][j+1] in ['0','1','2','3','4','5','6','7','8','9']:
                chiffres.append([i,j+1])
    if i < len(lignes)-1:
        if j > 0:
            if lignes[i+1][j-1] in ['0','1','2','3','4','5','6','7','8','9']:
                chiffres.append([i+1,j-1])
        if lignes[i+1][j] in ['0','1','2','3','4','5','6','7','8','9']:
                chiffres.append([i+1,j])
        if j < len(lignes[0]) -1:
            if lignes[i+1][j+1] in ['0','1','2','3','4','5','6','7','8','9']:
                chiffres.append([i+1,j+1])
    return chiffres 

def suppression_double_chiffre(next_numbers,coord_etoile):
    result = [next_numbers[0]]
    i = next_numbers[0][0]
    j = next_numbers[0][1]
    for k in range(1,len(next_numbers)):
        if next_numbers[k][0] == i: #pas de changement de ligne
            if coord_etoile[0] == i:
                result.append(next_numbers[k])
            #decalage de j de + de 1 case ET case d'avant pas dans next_numbers
            elif next_numbers[k][1] != j+1 and [i,next_numbers[k][1]-1] not in next_numbers:
                result.append(next_numbers[k])
                j = next_numbers[k][1]
        else:
            i = next_numbers[k][0]
            j = next_numbers[k][1]
            result.append(next_numbers[k])
    return result

def presence_autres_chiffres(lignes,i,j):
    '''
    :return: tab de coord [i,j] des chiffres trouves
    '''
    reponse = []
    while j > 0 and lignes[i][j-1] in ['0','1','2','3','4','5','6','7','8','9']:
        j -= 1
    while j < len(lignes[0]) and lignes[i][j] in ['0','1','2','3','4','5','6','7','8','9']:
        reponse.append([i,j])
        j += 1
    return reponse

def transformation_tabcoord_nombre(lignes,nombre_coords):
    nombre = 0
    decrem = len(nombre_coords)-1
    for coord in nombre_coords:
        nombre += int(lignes[coord[0]][coord[1]])*10**decrem
        decrem -= 1
    return nombre

def recherche_gears(lignes):
    somme = 0
    for i in range(len(lignes)):
        j = 0
        while j < len(lignes[0]):
            if lignes[i][j] == '*':
                product = 1
                near_numbers = chiffres_autour(lignes,[i,j])
                uniq_numbers = suppression_double_chiffre(near_numbers,[i,j])
                if len(uniq_numbers) >= 2: #2 nombres autour
                    for coord_chiffre in uniq_numbers:
                        nombre_coords = presence_autres_chiffres(lignes,coord_chiffre[0],coord_chiffre[1])
                        nombre_entier = transformation_tabcoord_nombre(lignes,nombre_coords)
                        print(nombre_entier)
                        product = product * nombre_entier
                if product != 1:
                    somme += product
            j += 1
    return somme



    
print(recherche_gears(lignes)) #Pas Bon