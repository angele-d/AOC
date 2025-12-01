
from enum import Enum

class DirectionType(Enum):
    HAUT = 0
    DROITE = 1
    BAS = 2
    GAUCHE = 3

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

def searchAroundTabCoord(tab,coord):
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

def findAreaPerimeter(coordBase):
    area,nombre_collisions = findArea(coordBase)
    for coord in area:
        garden[coord[0]][coord[1]] = "#"
    nbArea = len(area)
    nbPerimeter = nbArea * 4 - nombre_collisions
    return nbArea,nbPerimeter

def findNewPlot():
    areaPerimeterRegister= []
    areaPerimeterRegister.append(findAreaPerimeter((0,0)))
    for i in range (len(garden)):
        for j in range (len(garden[i])):
            lettre = garden[i][j]
            if lettre != "#": #Nouvelle region d'une lettre
                areaPerimeterRegister.append(findAreaPerimeter((i,j)))
    return areaPerimeterRegister     

def calculPrice():
    areaPerimeterRegister = findNewPlot()
    somme = 0
    for plot in areaPerimeterRegister:
        fact = plot[0] * plot[1]
        somme += fact
    return somme

def main(contenu):
    global garden
    garden = returnLinesInTabxTab(splitFile("\n",readFile(contenu)))
    return calculPrice()

print(main("datas/2024_day12_exemple1"))
print(main("datas/2024_day12_exemple3"))
print(main("datas/2024_day12_data"))