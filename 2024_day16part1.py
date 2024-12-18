import sys
from enum import Enum
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

def searchMinimumChemin(labyrinthe,debut,fin):
    minChemin = {}
    def recursivite(coord,direction,acc = 0):
        xCoord,yCoord = coord
        if coord == fin: return acc
        elif labyrinthe[xCoord][yCoord] == "#": return 100000000000000
        elif coord in minChemin and minChemin[coord] <= acc: return 10000000000000000
        else:
            minChemin[coord] = acc

            allChemin = []
            for oneDirection in DirectionType:
                xNext,yNext = oneDirection.value
                if oneDirection == direction:
                    allChemin.append(recursivite((xCoord+xNext,yCoord+yNext),oneDirection,acc + 1))
                else:
                    allChemin.append(recursivite((xCoord+xNext,yCoord+yNext),oneDirection,acc +1001))
            return min(allChemin)
    return recursivite(debut,DirectionType.RIGHT)

def main(chemin):
    labyrinthe = returnLinesInTabxTab(splitFile("\n",readFile(chemin)))
    debut = searchUniqELT(labyrinthe,"S")
    fin = searchUniqELT(labyrinthe,"E")
    scoreMin = searchMinimumChemin(labyrinthe,debut,fin)
    return scoreMin

print(main("datas/2024_day16_data"))
#print(main("datas/2024_day16_exemple1"))