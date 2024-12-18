
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

def findOtherCroch(coord):
    x,y = coord
    if place[x][y-1] == "[": return (x,y-1)
    if place[x][y+1] == "]": return (x,y+1)
    print("Pb findOtherCroch")

def upCase(coord,otherCroch):
    coordParcourus = []
    dicoNewSymbols = {coord: '.', otherCroch: '.'}
    a_parcourir = [coord,otherCroch]
    while a_parcourir != []:
        x,y = a_parcourir[0]
        a_parcourir = a_parcourir[1:]
        if place[x][y] == '#':
            return None
        elif place[x][y] == '.':
            pass #On va passer jusqu'a esperer avoir a_parcourir vide
        else: #[ ou ]
            nextCoord = ((x-1,y))
            dicoNewSymbols[nextCoord] = place[x][y]
            a_parcourir.append(nextCoord)
            if place[nextCoord[0]][nextCoord[1]] in ['[',']']:
                nextCoordOtherCroch = findOtherCroch(nextCoord)
                if dicoNewSymbols.get(nextCoordOtherCroch) == None:
                    dicoNewSymbols[nextCoordOtherCroch] = '.'
                a_parcourir.append(nextCoordOtherCroch)
        coordParcourus.append((x,y))
    #Arrivee ici: On peut faire le deplacement
    for coordP in coordParcourus: #Reinitialise tout
        place[coordP[0]][coordP[1]] = '.'
    keys = dicoNewSymbols.keys()
    for key in keys:
        place[key[0]][key[1]] = dicoNewSymbols[key]
    return coord

def downCase(coord,otherCroch):
    coordParcourus = []
    dicoNewSymbols = {coord: '.', otherCroch: '.'}
    a_parcourir = [coord,otherCroch]
    while a_parcourir != []:
        x,y = a_parcourir[0]
        a_parcourir = a_parcourir[1:]
        if place[x][y] == '#':
            return None
        elif place[x][y] == '.':
            pass #On va passer jusqu'a esperer avoir a_parcourir vide
        else: #[ ou ]
            nextCoord = ((x+1,y))
            dicoNewSymbols[nextCoord] = place[x][y]
            a_parcourir.append(nextCoord)
            if place[nextCoord[0]][nextCoord[1]] in ['[',']']:
                nextCoordOtherCroch = findOtherCroch(nextCoord)
                if dicoNewSymbols.get(nextCoordOtherCroch) == None:
                    dicoNewSymbols[nextCoordOtherCroch] = '.'
                a_parcourir.append(nextCoordOtherCroch)
        coordParcourus.append((x,y))
    #Arrivee ici: On peut faire le deplacement
    for coordP in coordParcourus: #Reinitialise tout
        place[coordP[0]][coordP[1]] = '.'
    keys = dicoNewSymbols.keys()
    for key in keys:
        place[key[0]][key[1]] = dicoNewSymbols[key]
    return coord

def moveCrochet(direction,nextCoord):
    xInit,yInit = nextCoord
    x,y = nextCoord
    match direction:
        case Direction.UP.value:
            otherCroch = findOtherCroch(nextCoord)
            if place[xInit][yInit] == '#' or place[otherCroch[0]][otherCroch[1]] == '#':
                return None
            else:
                return upCase(nextCoord,otherCroch)
        case Direction.DOWN.value:
            otherCroch = findOtherCroch(nextCoord)
            if place[xInit][yInit] == '#' or place[otherCroch[0]][otherCroch[1]] == '#':
                return None
            else:
                return downCase(nextCoord,otherCroch)
        case Direction.LEFT.value:
            while isInTable(place,(x,y-1)):
                if place[x][y-1] in ['[',']']:
                    y = y-1
                elif place[x][y-1] == '#':
                    return None
                else: #'.'
                    for j in range (y-1,yInit):
                        place[xInit][j] = place[xInit][j+1]
                    return xInit,yInit
            return None
        case Direction.RIGHT.value:
            while isInTable(place,(x,y+1)):
                if place[x][y+1] in ['[',']']:
                    y = y+1
                elif place[x][y+1] == '#':
                    return None
                else: #'.'
                    for j in reversed(range(yInit+1, y+2)):
                        place[xInit][j] = place[xInit][j-1]
                    return xInit,yInit
            return None
        case _:
            print("Pb moveO")

def makeMove(direction,nextCoord):
    x,y = nextCoord
    match place[x][y]:
        case '#':
            return None
        case '[':
            return moveCrochet(direction,nextCoord)
        case ']':
            return moveCrochet(direction,nextCoord)
        case '.':
            return (x,y)
        case _:
            print("Pb makeMove")

def parcours(direction,lanternFish):
    '''
    for k in range (len(place)):
        print(place[k])
    '''
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
        '''
        print(f"Move:{direction[i]}")
        for k in range (len(place)):
            print(place[k])  
        '''

def transcriptionNews(chemin):
    contenu = splitWhenEmptyLine(splitFile("\n",readFile(chemin)))
    place = contenu[0]
    directions = contenu[1]
    direction = ''
    for i in range (len(directions)):
        direction = direction+directions[i]
    for i in range (len(place)):
        place[i] = list(place[i])
    #########Debut transcription
    newPlace = []
    for i in range (len(place)):
        newPlaceLigne = ['R'] * len(place[i])*2
        for j in range (len(place)):
            match place[i][j]:
                case "#":
                    newPlaceLigne[2*j] = '#'
                    newPlaceLigne[2*j+1] = '#'
                case "O":
                    newPlaceLigne[2*j] = '['
                    newPlaceLigne[2*j+1] = ']'   
                case ".":
                    newPlaceLigne[2*j] = '.'
                    newPlaceLigne[2*j+1] = '.'    
                case "@":
                    newPlaceLigne[2*j] = '@'
                    newPlaceLigne[2*j+1] = '.'   
                case _: 
                    print("Pb transcriptionNews")         
        newPlace.append(newPlaceLigne)
    return newPlace,direction

def main(chemin):
    global place
    place,direction = transcriptionNews(chemin)
    parcours(direction,findLanternFish())
    coordsCrochGauche = searchELT(place,'[')
    sumGPScoordinates = 0
    for coord in coordsCrochGauche:
        sumGPScoordinates += 100*coord[0]+coord[1]
    return sumGPScoordinates
    

    
print(main("datas/2024_day15_data"))
#print(main("datas/2024_day15_exemple1")) #smaller
#print(main("datas/2024_day15_exemple2")) #larger
#print(main("datas/2024_day15_exemple3")) #part2