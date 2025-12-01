
from enum import Enum

class DirectionType(Enum): 
    #x : de gauche à droite
    #y : de haut en bas
    LEFT = (-1,0)
    RIGHT = (1,0)
    UP = (0,-1)
    DOWN = (0,1)

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

def tabInt(tab: list[str]):
    '''Passe les elts de tab en type int'''
    return [int(elt) for elt in tab]

def isInTableByLen(coord:tuple[int,int],xmax:int,ymax:int) -> bool:
    '''Verifie si les coord sont bien dans table et renvoie la valeur'''
    if (0 <= coord[0] <= xmax) and (0 <= coord[1] <= ymax):
        return True 
    else: return False

#-------------#

def Dijkstra(dicoCorrupted : dict[tuple[int,int],str], startCoord : tuple[int,int], endCoord : tuple[int,int]):
    distStart = {}
    distStart[startCoord] = 0
    a_traiter = [[startCoord[0],startCoord[1],0]] #[x,y,distStart]
    while a_traiter != []:
        xCurrent,yCurrent,distCurrent = a_traiter[0]
        a_traiter = a_traiter[1:]
        if distStart[(xCurrent,yCurrent)] >= distCurrent:
            for direction in DirectionType:
                xMove,yMove = direction.value
                nextCoord = (xMove+xCurrent,yMove+yCurrent)
                if isInTableByLen(nextCoord,maxX,maxY) and tuple(nextCoord) not in dicoCorrupted:
                    if distStart.get(nextCoord) == None or distStart[nextCoord] > distCurrent+1:
                        a_traiter.append([nextCoord[0],nextCoord[1],distCurrent+1])
                        distStart[nextCoord] = distCurrent+1
    return distStart.get(endCoord)    

def defineMemorySpace(coordList):
    DicoCorrupted = {}
    for coord in coordList:
        x,y = coord
        DicoCorrupted[x,y] = "#"
    return DicoCorrupted

def affichage(dicoCorrupted):
    tab = ['.'] * (maxY+1)
    for i in range (len(tab)):
        tab[i] = ['.']*(maxX+1)
    for key in dicoCorrupted:
        tab[key[1]][key[0]] = '#'
    for ligne in tab:
        print(ligne)
    

def main(chemin,nbBytes):
    contenu = splitFile("\n",readFile(chemin))
    for i in range (len(contenu)):
        contenu[i] = tabInt(splitFile(",",contenu[i]))
    dicoCorrupted = defineMemorySpace(contenu[:nbBytes])
    #affichage(dicoCorrupted)
    while Dijkstra(dicoCorrupted,(0,0),(maxX,maxY)) != None:
        nbBytes += 1
        dicoCorrupted[tuple(contenu[nbBytes])] = "#"

    return contenu[nbBytes]

jeuDeTest = "data"
match jeuDeTest:
    case "data":
        maxX = 70 #INCLUS
        maxY = 70 
        print(main("datas/2024_day18_data",1024))
    case "exemple":
        maxX = 6 #INCLUS
        maxY = 6
        print(main("datas/2024_day18_exemple",12))

