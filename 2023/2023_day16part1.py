
fichier = open("datas/2023_day16_exemple","r")

lignes = fichier.readlines()
for i in range (len(lignes)):
    lignes[i] = lignes[i][:-1]

transformation_tableau = [[]] * len(lignes)
for i in range (len(lignes)):
    transformation_tableau[i] = ['.'] * len(lignes[i])
    for j in range (len(lignes[i])):
        transformation_tableau[i][j] = lignes[i][j]


def next_step_H(grille,x,y):
    '''
    :return: tableau de tableau [[x,y,direction],...]
    '''
    if x-1 < 0:
            return [[-1,-1,'N']] #N = None ; Pas de suite
    else:
        if grille[x-1][y] == "\\" and y-1>=0:
            return [[x-1,y-1,'G']]
        if grille[x-1][y] == "/" and y+1<len(grille[0]):
            return [[x-1,y+1,'D']]
        if grille[x-1][y] == "-":
            if y-1 >= 0 and y+1 < len(grille[0]):
                return [[x-1,y-1,'G'],[x-1,y+1,'D']]
            elif y-1 >= 0:
                    return [[x-1,y-1,'G']]
            elif y+1 < len(grille[0]):
                return [[x-1,y+1,'D']]
        if grille[x-1][y] == "|" and x-2>=0:
            return [[x-2,y,'H']]
        if grille[x-1][y] == ".":
            return [[x-1,y,'H']]
        return [[-1,-1,'N']] #les 'and' ont echoue -> hors grille

def next_step_B(grille,x,y):
    '''
    :return: tableau de tableau [[x,y,direction],...]
    '''
    if x+1 >= len(grille):
            return [[-1,-1,'N']] #N = None ; Pas de suite
    else:
        if grille[x+1][y] == "\\" and y+1<len(grille[0]):
            return [[x+1,y+1,'D']]
        if grille[x+1][y] == "/" and y-1>=0:
            return [[x+1,y-1,'G']]
        if grille[x+1][y] == "-":
            if y-1 >= 0 and y+1 < len(grille[0]):
                return [[x+1,y-1,'G'],[x-1,y+1,'D']]
            elif y-1 >= 0:
                return [[x+1,y-1,'G']]
            elif y+1 < len(grille[0]):
                return [[x+1,y+1,'D']]
        if grille[x+1][y] == "|" and x+2< len(grille):
            return [[x+2,y,'B']]
        if grille[x+1][y] == ".":
            return [[x+1,y,'B']]
        return [[-1,-1,'N']] #les 'and' ont echoue -> hors grille

def next_step_G(grille,x,y):
    '''
    :return: tableau de tableau [[x,y,direction],...]
    '''
    if y-1 < 0:
            return [[-1,-1,'N']] #N = None ; Pas de suite
    else:
        if grille[x][y-1] == "\\" and x-1>=0:
            return [[x-1,y-1,'H']]
        if grille[x][y-1] == "/" and x+1<len(grille):
            return [[x+1,y-1,'B']]
        if grille[x][y-1] == "-" and y-2>= 0:
            return [[x,y-2,'G']]
        if grille[x][y-1] == "|":
            if x-1 >= 0 and x+1 < len(grille):
                return [[x-1,y-1,'H'],[x+1,y-1,'B']]
            elif x-1 >= 0:
                return [[x-1,y-1,'H']]
            elif x+1 < len(grille):
                return [[x+1,y-1,'B']]
        if grille[x][y-1] == ".":
            return [[x,y-1,'G']]
        return [[-1,-1,'N']] #les 'and' ont echoue -> hors grille        

def next_step_D(grille,x,y):
    '''
    :return: tableau de tableau [[x,y,direction],...]
    '''
    if y+1 >= len(grille[0]):
            return [[-1,-1,'N']] #N = None ; Pas de suite
    else:
        if grille[x][y+1] == "\\" and x+1<len(grille):
            return [[x+1,y+1,'B']]
        if grille[x][y+1] == "/" and x-1>=0:
            return [[x-1,y+1,'H']]
        if grille[x][y+1] == "-" and y+2<len(grille[0]):
            return [[x,y+2,'D']]
        if grille[x][y+1] == "|":
            if x-1 >= 0 and x+1 < len(grille):
                return [[x-1,y+1,'H'],[x+1,y+1,'B']]
            elif x-1 >= 0:
                return [[x-1,y+1,'H']]
            elif x+1 < len(grille):
                return [[x+1,y+1,'B']]
        if grille[x][y+1] == ".":
            return [[x,y+1,'D']]
        return [[-1,-1,'N']] #les 'and' ont echoue -> hors grille  

def tabxtab_de_0(grille):
    tab = [0] * len(grille)
    for i in range (len(grille)):
        tab[i] = [0] * len(grille[0])
    return tab

def est_valide(grille, elt, nb_parcours):
    x,y,direction = elt
    if (elt[0] == -1 or elt[1] == -1) or nb_parcours[x][y] >= 2:
        return False
    match direction:
        case "H":
            if grille[x][y] in ["H","B"]:
                return False
        case "B":
            if grille[x][y] in ["H","B"]:
                return False
        case "G":
            if grille[x][y] in ["G","D"]:
                return False
        case "D":
            if grille[x][y] in ["G","D"]:
                return False
        case _:
            return True
    return True

def calcul_energized(nb_parcours):
    nb_energized = 0
    for i in range (len(nb_parcours)):
        for j in range (len(nb_parcours[i])):
            if nb_parcours[i][j] > 0:
                nb_energized += 1
    return nb_energized

def parcours(grille, coords):
    file_parcours = [coords]
    nb_parcours = tabxtab_de_0(grille)
    while file_parcours != []:
        x,y = file_parcours[0]
        nb_parcours[x][y] = nb_parcours[x][y] + 1
        file_parcours = file_parcours[1:]

        direction = grille[x][y]
        match direction:
            case 'H':
                next_step = next_step_H(grille,x,y)
                for elt in next_step:
                    if est_valide(grille, elt, nb_parcours):
                        grille[elt[0]][elt[1]] = elt[2]
                        file_parcours.append((elt[0],elt[1]))
            case 'B':
                next_step = next_step_B(grille,x,y)
                for elt in next_step:
                    if est_valide(grille, elt, nb_parcours):
                        grille[elt[0]][elt[1]] = elt[2]
                        file_parcours.append((elt[0],elt[1]))
            case 'G':
                next_step = next_step_G(grille,x,y)
                for elt in next_step:
                    if est_valide(grille, elt, nb_parcours):
                        grille[elt[0]][elt[1]] = elt[2]
                        file_parcours.append((elt[0],elt[1]))
            case 'D':
                next_step = next_step_D(grille,x,y)
                for elt in next_step:
                    if est_valide(grille, elt, nb_parcours):
                        grille[elt[0]][elt[1]] = elt[2]
                        file_parcours.append((elt[0],elt[1]))
            case _:
                print("Probleme")
    nb_energized = calcul_energized(nb_parcours)
    return nb_energized

def main_function(grille):
    '''
    :return: nombre de cases parcourues
    '''
    match grille[0][0]:
        case '.':
            grille[0][0] = 'D'
            return parcours(grille,(0,0))
        case '\\':
            grille[1][0] = 'B'
            return parcours(grille,(1,0))
        case '/':
            return grille
        case '-':
            grille[0][1] = 'D'
            return parcours(grille,(0,1))
        case '|':
            grille[1][0] = 'B'
            return parcours(grille,(1,0))
        case _:
            print("Probleme vers initialisation")
            return grille 
        
        


result = (main_function(transformation_tableau))
for i in range (len(result)):
    print(result[i])