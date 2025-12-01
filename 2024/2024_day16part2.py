import sys
from enum import Enum
import copy
sys.setrecursionlimit(10000)

class DirectionType(Enum):
    RIGHT = (0,1)
    DOWN = (1,0)
    LEFT = (0,-1)
    UP = (-1,0)

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

def searchUniqELT(table,elt):
    '''Trouve l'elt dans la table'''
    for i in range (len(table)):
        for j in range (len(table[i])):
            if table[i][j] == elt:
                return i,j
    return None

#--------------#

'''
def getDimensions(table : list[str], mur: dict[tuple[int,int],bool]) -> tuple[int,int,int,int]:
    endY, endX =0,0
    coordY, coordX =0,0
    for idx in range(len(table)):
        for jdx in range(len(table[idx])) :
            
            if table[idx][jdx]=='#' :mur[(idx,jdx)]= True
            elif table[idx][jdx]=='E':   endY, endX =(idx,jdx)
            elif table[idx][jdx]=='S':  coordY, coordX =(idx,jdx)

    return ( coordY, coordX, endY, endX)

def getAllPath(y : int, x : int , endY : int, endX : int, mur  : dict[tuple[int,int],bool]) -> int : 
    endPath :  dict[tuple[int,int], dict[tuple[int,int],bool]] = {}
    minimumValue = {}
    othersPath = {}
    def recurs(coordY: int, coordX : int,acc: int, chemin : dict[tuple[int,int],bool],direction : DirectionType)-> int :
        print(acc)
        if coordY == endY and coordX == endX :
            if acc in endPath :endPath[acc] = endPath[acc] | chemin
            else :
                chemin[(coordY, coordX)]=True
                endPath[acc] = chemin
            return acc
        if (coordY, coordX) in mur : return 100000000000
        if (coordY, coordX) in minimumValue and  minimumValue[(coordY, coordX)] <= acc   :
            if minimumValue[(coordY, coordX)]+1000 == acc or minimumValue[(coordY, coordX)] == acc : 
                othersPath[(coordY, coordX)] = chemin
            return 100000000000
                
        minimumValue[(coordY, coordX)]=acc
        chemin[(coordY, coordX)]=True

        path = []
        for newDirection in DirectionType : 
            newY, newX = newDirection.value
            if newDirection.value == direction.value : path.append(recurs(coordY+newY, coordX+newX,acc+1,copy.deepcopy(chemin),newDirection))        
            else : path.append(recurs(coordY+newY, coordX+newX,acc+1001,copy.deepcopy(chemin),newDirection))

        return min(path)

    minimum = recurs(y,x, 0,{},DirectionType.DROITE )
    res = copy.deepcopy(endPath[minimum])
    for key in endPath[minimum] :
        if key in othersPath :
            print(othersPath[key])
            for otherKey in othersPath[key] : 
                if otherKey not in res:res[otherKey] = True 

    return len(res.keys())
    
def tilesOfTheBestWay(chemin : str) -> int:
    table = splitFile(
            '\n', 
            readFile(chemin)
        )
    mur = {}

    coordY , coordX, endY, endX = getDimensions(table,mur)

    return getAllPath(coordY,coordX, endY, endX, mur)

print(tilesOfTheBestWay("datas/2024_day16_exemple1"))
'''
'''
def searchAllMinimumChemin(labyrinthe, depart : tuple[int,int] , end : tuple[int,int],) -> int : 
    endChemin :  dict[int, dict[tuple[int,int],bool]] = {}
    minimumValue = {}
    othersChemins = {}
    endX,endY = end
    def recursivite(coord : tuple[int,int],acc: int, chemin : dict[tuple[int,int],bool],direction : DirectionType)-> int :
        coordX, coordY = coord
        if coordY == endY and coordX == endX :
            if acc in endChemin :endChemin[acc] = endChemin[acc] | chemin
            else :
                chemin[(coordX, coordY)]=True
                endChemin[acc] = chemin
            return acc
        if labyrinthe[coordX][coordY] : return 100000000000
        if (coordX, coordY) in minimumValue and  minimumValue[(coordX, coordY)] <= acc   :
            if minimumValue[(coordX, coordY)]+1000 == acc or minimumValue[(coordX, coordY)] == acc : 
                othersChemins[(coordX, coordY)] = chemin
            return 100000000000
                
        minimumValue[(coordX, coordY)]=acc
        chemin[(coordX, coordY)]=True

        path = []
        for newDirection in DirectionType : 
            newX, newY = newDirection.value
            if newDirection.value == direction.value : path.append(recursivite(coordY+newY, coordX+newX,acc+1,copy.deepcopy(chemin),newDirection))        
            else : path.append(recursivite([coordX+newX,coordY+newY],acc+1001,copy.deepcopy(chemin),newDirection))

        return min(path)

    minimum = recursivite(depart, 0,{},DirectionType.RIGHT )
    res = endChemin[minimum]
    for key in endChemin[minimum] :
        if key in othersChemins :
            print(othersChemins[key])
            for otherKey in othersChemins[key] : 
                if otherKey not in res:res[otherKey] = True 

    return len(res.keys())

'''
def searchAllMinimumChemin(labyrinthe,debut,fin):
    minValue : dict[tuple[int,int],int] = {}
    endChemin : dict[int,dict[tuple[int,int],bool]] = {}
    allChemin : dict[tuple[int,int],dict[tuple[int,int],bool]] = {}
    def recursivite(coord,direction,chemin : dict[tuple[int,int],bool],acc = 0):
        xCoord,yCoord = coord
        if coord == fin: 
            if acc in endChemin: endChemin[acc] = endChemin[acc] | chemin
            else:
                chemin[coord] = True
                endChemin[acc] = chemin
            return acc
        elif labyrinthe[xCoord][yCoord] == "#": 
            return 100000000000000
        elif coord in minValue and minValue[coord] <= acc: 
            if minValue[coord] == acc or minValue[coord]+1000 == acc:
                allChemin[coord] = chemin
                return 1000000000000
        else:
            minValue[coord] = acc
            chemin[coord] = True

            chemins = []
            for oneDirection in DirectionType:
                xNext,yNext = oneDirection.value
                if oneDirection == direction:
                    chemins.append(recursivite((xCoord+xNext,yCoord+yNext),oneDirection,copy.deepcopy(chemin),acc + 1))
                else:
                    chemins.append(recursivite((xCoord+xNext,yCoord+yNext),oneDirection,copy.deepcopy(chemin),acc +1001))
            print(chemins)
            return min(chemins)
        
    minValuePath = recursivite(debut,DirectionType.RIGHT,{})
    cheminCorrespondants = copy.deepcopy(endChemin[minValuePath])
    print(cheminCorrespondants)


def main(chemin):
    labyrinthe = returnLinesInTabxTab(splitFile("\n",readFile(chemin)))
    debut = searchUniqELT(labyrinthe,"S")
    fin = searchUniqELT(labyrinthe,"E")
    scoreMin = searchAllMinimumChemin(labyrinthe,debut,fin)
    return scoreMin

#print(main("datas/2024_day16_data"))
print(main("datas/2024_day16_exemple1"))
