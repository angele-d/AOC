
fichier = open("datas/2024_day4_data","r")

lignes = fichier.readlines()
for i in range (len(lignes)-1):
    lignes[i] = lignes[i][:-1]

def find_M(lignes,i,j):
    indices = []
    if j > 0:
        if lignes[i][j-1] == "M":
            indices.append([i,j-1,"G"])
    if j < len(lignes[0])-1:
        if lignes[i][j+1] == "M":
            indices.append([i,j+1,"D"])    
    if i > 0:
        if lignes[i-1][j] == "M":
            indices.append([i-1,j,"H"])
        if j > 0:
            if lignes[i-1][j-1] == "M":
                indices.append([i-1,j-1,"HG"])
        if j < len(lignes[0]) -1:
            if lignes[i-1][j+1] == "M":
                indices.append([i-1,j+1,"HD"])
    if i < len(lignes)-1:
        if lignes[i+1][j] == "M":
                indices.append([i+1,j,"B"])
        if j > 0:
            if lignes[i+1][j-1] == "M":
                indices.append([i+1,j-1,"BG"])
        if j < len(lignes[0]) -1:
            if lignes[i+1][j+1] == "M":
                indices.append([i+1,j+1,"BD"])
    return indices

def find_AS(lignes,i,j,direction,lettre):
    match direction:
        case "B":
            if i+1 < len(lignes) and lignes[i+1][j] == lettre:
                return [i+1,j]
            else:
                return []
        case "H":
            if i-1 >= 0 and lignes[i-1][j] == lettre:
                return [i-1,j]
            else:
                return []
        case "G":
            if j-1 >= 0 and lignes[i][j-1] == lettre:
                return [i,j-1]
            else:
                return []
        case "D":
            if j+1 < len(lignes[i]) and lignes[i][j+1] == lettre:
                return [i,j+1]
            else:
                return []
        case "HG":
            if i-1 >= 0 and j-1 >= 0 and lignes[i-1][j-1] == lettre:
                return [i-1,j-1]
            else:
                return []
        case "BG":
            if i+1 < len(lignes) and j-1 >= 0 and lignes[i+1][j-1] == lettre:
                return [i+1,j-1]
            else:
                return []
        case "HD":
            if i-1 >= 0 and j+1 < len(lignes[i-1]) and lignes[i-1][j+1] == lettre:
                return [i-1,j+1]
            else:
                return []
        case "BD":
            if i+1 < len(lignes) and j+1 < len(lignes[i+1]) and lignes[i+1][j+1] == lettre:
                return [i+1,j+1]
            else:
                return []
        case _:
            print("Problème")

def autour_A(lignes,i,j):
    if i == 0 or i == len(lignes)-1 or j == 0 or j == len(lignes)-1:
        return False
    else:
        if lignes[i-1][j-1] == "M" and lignes[i+1][j+1] == "S":
            if lignes[i-1][j+1] == "M" and lignes[i+1][j-1] == "S":
                return True
            if lignes[i-1][j+1] == "S" and lignes[i+1][j-1] == "M":
                return True
        if lignes[i-1][j-1] == "S" and lignes[i+1][j+1] == "M":
            if lignes[i-1][j+1] == "M" and lignes[i+1][j-1] == "S":
                return True
            if lignes[i-1][j+1] == "S" and lignes[i+1][j-1] == "M":
                return True
        return False

def recherche_MAS(lignes):
    nb_occurence = 0
    for i in range (len(lignes)):
        for j in range (len(lignes[i])):
            if lignes[i][j] == "A":
                if autour_A(lignes,i,j):
                    nb_occurence += 1
    return nb_occurence

print(recherche_MAS(lignes))
