
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

def recherche_XMAS(lignes):
    nb_occurence = 0
    for i in range (len(lignes)):
        for j in range (len(lignes[i])):
            if lignes[i][j] == "X":
                M_present = find_M(lignes,i,j)
                print(f"X: {i} {j} M: {M_present}")
                for M in M_present:
                    A = find_AS(lignes,M[0],M[1],M[2],"A")
                    print(f"M: {M[0]} {M[1]} A: {A}")
                    if A != []:
                        S = find_AS(lignes,A[0],A[1],M[2],"S")
                        print(f"A: {A[0]} {A[1]} S: {S}")
                        if S != []:
                            nb_occurence += 1
    return nb_occurence

print(recherche_XMAS(lignes))
