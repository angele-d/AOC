

def readFile(chemin):
    '''Lecture d'un fichier'''
    fichier = open(chemin,"r")
    return fichier.read()

def splitFile(separateur: str,contenu):
    '''Split d'un fichier selon separateur'''
    return contenu.split(separateur)

def returnLines(contenu):
    '''Renvoie les lignes du fichier sous forme de tab de tab'''
    lines = [list(ligne) for ligne in contenu]
    if lines[-1] == []: #Cas où derniere ligne du fichier est vide
        return lines[:-1]
    return lines

def tableInt(table):
    '''Passe les elts de table en type int'''
    new_table = []
    for i in range (len(table)):
        new_table.append([int(elt) for elt in table[i]])
    return new_table

def isInTable(table,coord):
    '''Verifie si les coord sont bien dans table et renvoie la valeur'''
    if (0 <= coord[0] < len(table)) and (0 <= coord[1] < len(table[coord[0]])):
        return table[coord[0]][coord[1]]
    else: return None

def searchAround(table,coord):
    '''Renvoie valeur_coord[haut,droite,bas,gauche] de coord'''
    x,y = coord
    haut = isInTable(table,(x-1,y))
    droite = isInTable(table,(x,y+1))
    bas = isInTable(table,(x+1,y))
    gauche = isInTable(table,(x,y-1))
    return [haut,droite,bas,gauche]

#------------------------------------------#

def search0(table):
    '''Trouve les 0 dans la table'''
    coords0 = []
    for i in range (len(table)):
        for j in range (len(table[i])):
            if table[i][j] == 0:
                coords0.append((i,j))
    return coords0    

def scoreTrailhead(table,coord):
    '''Renvoie le score d'1 trailhead'''
    coord9 = []
    def step(table,number,coord):
        x,y = coord
        dicoAssocDirection = {0:(x-1,y), 1:(x,y+1), 2:(x+1,y), 3:(x,y-1)}
        if number == 9:
            if coord not in coord9: coord9.append(coord)
        else:
            nextnumber = number+1
            nbAround = searchAround(table,coord)
            countNextNumber = nbAround.count(nextnumber)
            print(f"{number}:{nbAround}->{countNextNumber}")
            if countNextNumber == 0: pass
            else:
                for i in range (len(nbAround)):
                    if nbAround[i] == nextnumber:
                        print(f"{nextnumber},{dicoAssocDirection[i]}")
                        step(table,nextnumber,dicoAssocDirection[i])
    step(table,0,coord)
    return coord9

def main(chemin):
    table = returnLines(splitFile("\n",readFile(chemin)))
    table = tableInt(table)
    ensemble0 = search0(table)
    allCoord9 = []
    for coord0 in ensemble0:
        coord9 = scoreTrailhead(table,coord0)
        allCoord9 = allCoord9 + coord9
    return len(allCoord9)
    


print(main("datas/2024_day10_data"))