
from enum import Enum

class Direction(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

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

def tableInt(table):
    '''Passe les elts de table en type int'''
    new_table = []
    for i in range (len(table)):
        new_table.append([int(elt) for elt in table[i]])
    return new_table

def splitWhenEmptyLine(contenu : list[str]) -> list[list[str]]:
    '''Split le tableau selon la presence ou non d'une ligne '' 
    >>> splitWhenEmptyLine(["a","b","c","","d","e","f"])
    [["a","b","c"],["d","e","f"]]
    '''
    nbLigneWithoutEmptyLine = 0
    result = []
    for i in range (len(contenu)):
        if contenu[i] == '':
            result.append([contenu[k] for k in range (i-nbLigneWithoutEmptyLine,i)])
            nbLigneWithoutEmptyLine = 0
        else:
            nbLigneWithoutEmptyLine += 1
    result.append([contenu[k] for k in range (len(contenu)-nbLigneWithoutEmptyLine,len(contenu))])
    return result

def isInTable(table,coord):
    '''Verifie si les coord sont bien dans table et renvoie la valeur'''
    if (0 <= coord[0] < len(table)) and (0 <= coord[1] < len(table[coord[0]])):
        return table[coord[0]][coord[1]]
    else: return None

def searchELT(table,elt):
    '''Trouve les elt dans la table'''
    coordsELT = []
    for i in range (len(table)):
        for j in range (len(table[i])):
            if table[i][j] == elt:
                coordsELT.append((i,j))
    return coordsELT 

#---------------#

def findLanternFish():
    for i in range (len(place)):
        if "@" in place[i]:
            for j in range (len(place[i])):
               if place[i][j] == "@":
                   return (i,j)
    print("Problème dans findLanternFish") #problème

def moveO(direction,nextCoord):
    xInit,yInit = nextCoord
    x,y = nextCoord
    match direction:
        case Direction.UP.value:
            while isInTable(place,(x-1,y)):
                if place[x-1][y] == 'O':
                    x = x-1
                elif place[x-1][y] == '#':
                    return None
                else: #place[x-1][y] == '.':
                    for i in range (x-1,xInit):
                        place[i][yInit] = 'O'
                    return xInit,yInit
            return None
        case Direction.DOWN.value:
            while isInTable(place,(x+1,y)):
                if place[x+1][y] == 'O':
                    x = x+1
                elif place[x+1][y] == '#':
                    return None
                else: #place[x+1][y] == '.':
                    for i in range (xInit+1,x+2):
                        place[i][yInit] = 'O'
                    return xInit,yInit
            return None
        case Direction.LEFT.value:
            while isInTable(place,(x,y-1)):
                if place[x][y-1] == 'O':
                    y = y-1
                elif place[x][y-1] == '#':
                    return None
                else: #place[x][y-1] == '.':
                    for j in range (y-1,yInit):
                        place[xInit][j] = 'O'
                    return xInit,yInit
            return None
        case Direction.RIGHT.value:
            while isInTable(place,(x,y+1)):
                if place[x][y+1] == 'O':
                    y = y+1
                elif place[x][y+1] == '#':
                    return None
                else: #place[x][y+1] == '.':
                    for j in range (yInit+1, y+2):
                        place[xInit][j] = 'O'
                    return xInit,yInit
            return None
        case _:
            print("Pb moveO")

def makeMove(direction,nextCoord):
    x,y = nextCoord
    match place[x][y]:
        case '#':
            return None
        case 'O':
            return moveO(direction,nextCoord)
        case '.':
            return (x,y)
        case _:
            print("Pb makeMove")

def parcours(direction,lanternFish):
    for i in range (len(direction)):
        match direction[i]:
            case Direction.UP.value:
                newPosFish = makeMove(direction[i],(lanternFish[0]-1,lanternFish[1]))
            case Direction.DOWN.value:
                newPosFish = makeMove(direction[i],(lanternFish[0]+1,lanternFish[1]))
            case Direction.LEFT.value:
                newPosFish = makeMove(direction[i],(lanternFish[0],lanternFish[1]-1))
            case Direction.RIGHT.value:
                newPosFish = makeMove(direction[i],(lanternFish[0],lanternFish[1]+1))
            case _:
                print("Pb parcours")
        if newPosFish != None:
            place[lanternFish[0]][lanternFish[1]] = '.'
            place[newPosFish[0]][newPosFish[1]] = '@'
            lanternFish = newPosFish

def main(chemin):
    global place
    contenu = splitWhenEmptyLine(splitFile("\n",readFile(chemin)))
    place = contenu[0]
    directions = contenu[1]
    direction = ''
    for i in range (len(directions)):
        direction = direction+directions[i]
    for i in range (len(place)):
        place[i] = list(place[i])
    parcours(direction,findLanternFish())
    coordsO = searchELT(place,'O')
    sumGPScoordinates = 0
    for coord in coordsO:
        sumGPScoordinates += 100*coord[0]+coord[1]
    return sumGPScoordinates
    

    
print(main("datas/2024_day15_data"))
#print(main("datas/2024_day15_exemple1"))
