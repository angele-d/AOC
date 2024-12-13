

def readFile(chemin):
    '''Lecture d'un fichier'''
    fichier = open(chemin,"r")
    return fichier.read()

def splitFile(separateur: str,contenu):
    '''Split d'un fichier selon separateur'''
    separation = contenu.split(separateur)
    #Derniere ligne vide
    if separation[-1] == "": separation = separation[:-1]
    #Fichier contient une seule ligne ?
    if len(separation) == 1: return separation[0]
    else: return separation

def returnLinesInTabxTab(contenu: list[str]):
    '''Renvoie les lignes du fichier sous forme de tab de tab'''
    lines = [list(ligne) for ligne in contenu]
    if lines[-1] == []: #Cas où derniere ligne du fichier est vide
        return lines[:-1]
    return lines

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

def searchAroundTabCoord(tab,coord: tuple[int]) -> list[tuple[int]]:
    '''Renvoie les valeurs_coord autour de coord qui sont dans tab'''
    x,y = coord
    around = []
    if (x-1,y) in tab: around.append((x-1,y))
    if (x,y+1) in tab: around.append((x,y+1))
    if (x+1,y) in tab: around.append((x+1,y))
    if (x,y-1) in tab: around.append((x,y-1))
    return around

def returnCoord(indice,coord):
    '''Renvoie les coordonnees correspondant à un indice de [0,3]'''
    x,y = coord
    match indice:
        case 0: return (x-1,y)
        case 1: return (x,y+1)
        case 2: return (x+1,y)
        case 3: return (x,y-1)
        case _ : print("Probleme returnCoord")

def TriTuples(tab):
    '''Tri un tableau de tuple selon coordonnees x puis y'''
    for i in range (len(tab)):
        min = i
        for j in range (i+1,len(tab)):
            if tab[min][0] > tab[j][0]: min = j
            elif tab[min][0] == tab[j][0]:
                if tab[min][1] > tab[j][1]: min = j
        if min != i:
            temp = tab[i]
            tab[i] = tab[min]
            tab[min] = temp
    return tab

def minMaxXYInArea(tab):
    '''Renvoie coord x min et max et coord y min et max d'un tableau de coordonnees'''
    minX = tab[0][0]
    maxX = tab[0][0]
    minY = tab[0][1]
    maxY = tab[0][1]
    for coord in tab:
        if coord[0] < minX: minX = coord[0]
        elif coord[0] > maxX: maxX = coord[0]
        if coord[1] < minY: minY = coord[1]
        elif coord[1] > maxY: maxY = coord[1]
    return minX,minY,maxX,maxY

#-------------------#

def findArea(coord):
    samePlotAround = [coord]
    nombre_collisions = 0
    x,y = coord
    plot = garden[x][y]
    file = [coord]
    while(file != []):
        #print(f"file{plot}: {file}")
        plotAround = searchAround(garden,file[0])
        for i in range (len(plotAround)):
            if plotAround[i] == plot:
                nombre_collisions += 1
                coordAround = returnCoord(i,file[0])
                if not coordAround in samePlotAround: 
                    if isInTable(garden,coordAround):
                        file.append(coordAround)
                        samePlotAround.append(coordAround)
        file = file[1:]
    return samePlotAround,nombre_collisions

def fourthInArea(coord1,coord2,area):
    if (min(coord1[0],coord2[0]),max(coord1[1],coord2[1])) not in area:
        return True
    elif (max(coord1[0],coord2[0]),min(coord1[1],coord2[1])) not in area:
        return True
    elif (max(coord1[0],coord2[0]),max(coord1[1],coord2[1])) not in area:
        return True
    elif (min(coord1[0],coord2[0]),min(coord1[1],coord2[1])) not in area:
        return True
    else:
        return False

def nbCorner(i,j,area):
    numCorner = 0
    if isInTable(garden,(i,j)):
        aroundIJ = searchAroundTabCoord(area,(i,j))
        #print(f"{i,j} around: {aroundIJ}")
        if len(aroundIJ) == 0: numCorner = 4
        if len(aroundIJ) == 1: numCorner = 2
        if len(aroundIJ) == 2:
            coord1 = aroundIJ[0]
            coord2 = aroundIJ[1]
            if (abs(coord1[0]-coord2[0]),abs(coord1[1]-coord2[1])) == (1,1): #Pas sur meme ligne
                numCorner = 1
                if fourthInArea(coord1,coord2,area): numCorner = 2
        if len(aroundIJ) == 3:
            coord1 = aroundIJ[0]
            coord2 = aroundIJ[1]
            coord3 = aroundIJ[2]
            if (abs(coord1[0]-coord2[0]),abs(coord1[1]-coord2[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord1,coord2,area): numCorner += 1
            if (abs(coord2[0]-coord3[0]),abs(coord2[1]-coord3[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord2,coord3,area): numCorner += 1 
            if (abs(coord1[0]-coord3[0]),abs(coord1[1]-coord3[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord1,coord3,area): numCorner += 1 
        if len(aroundIJ) == 4:
            coord1 = aroundIJ[0]
            coord2 = aroundIJ[1]
            coord3 = aroundIJ[2]
            coord4 = aroundIJ[3]
            if (abs(coord1[0]-coord2[0]),abs(coord1[1]-coord2[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord1,coord2,area): numCorner += 1
            if (abs(coord1[0]-coord3[0]),abs(coord1[1]-coord3[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord1,coord3,area): numCorner += 1
            if (abs(coord1[0]-coord4[0]),abs(coord1[1]-coord4[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord1,coord4,area): numCorner += 1
            if (abs(coord2[0]-coord3[0]),abs(coord2[1]-coord3[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord2,coord3,area): numCorner += 1
            if (abs(coord2[0]-coord4[0]),abs(coord2[1]-coord4[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord2,coord4,area): numCorner += 1
            if (abs(coord3[0]-coord4[0]),abs(coord3[1]-coord4[1])) == (1,1): #Pas sur meme ligne
                if fourthInArea(coord3,coord4,area): numCorner += 1
    #print(f"{i,j}:{numCorner}")
    return numCorner

def findSides(area):
    numCorner = 0
    for coord in area:
        numCorner += nbCorner(coord[0],coord[1],area)
    return numCorner

def findAreaSides(coordBase):
    area,nombre_collisions = findArea(coordBase)
    side = findSides(area)
    #print(area)
    for coord in area:
        garden[coord[0]][coord[1]] = "#"
    nbArea = len(area)
    #print(f"{coordBase} : {nbArea,side}")
    return nbArea,side

def findNewPlot():
    areaSideRegister= []
    areaSideRegister.append(findAreaSides((0,0)))
    for i in range (len(garden)):
        for j in range (len(garden[i])):
            lettre = garden[i][j]
            if lettre != "#": #Nouvelle region d'une lettre
                areaSideRegister.append(findAreaSides((i,j)))
    return areaSideRegister

def calculPrice():
    areaSideRegister = findNewPlot()
    somme = 0
    for plot in areaSideRegister:
        fact = plot[0] * plot[1]
        somme += fact
    return somme

def main(contenu):
    global garden
    garden = returnLinesInTabxTab(splitFile("\n",readFile(contenu)))
    return calculPrice()

#print(main("datas/2024_day12_exemple1"))
print(main("datas/2024_day12_exemple3"))
print(main("datas/2024_day12_data"))

'''
#print(findSides([(0, 0), (0, 1), (0, 2), (0, 3)])) #4
print("")
#print(findSides([(1, 0), (1, 1), (2, 0), (2, 1)])) #4
print("")
#print(findSides([(1, 2), (2, 2), (2, 3), (3, 3)])) #8
print("")
#print(findSides([(3, 0), (3, 1), (3, 2)])) #4
print("")
print(findSides([(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,2)])) #10
print("")
print(findSides([(0,1),(1,0),(1,1),(1,2),(2,1)]))
'''