import sys
from enum import Enum
sys.setrecursionlimit(10000)

class DirectionType(Enum): #x = lignes, y = colonnes
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

#------------------#

def parcoursPath(labyrinthe,start,end):
    dicoParcours = {}
    dicoParcours[start] = 0
    def recursivite(currentPos, acc = 1):
        if currentPos == end:
            pass
        else:
            for direction in DirectionType:
                addCoord = direction.value
                newCoord = (currentPos[0]+addCoord[0],currentPos[1]+addCoord[1])
                if labyrinthe[newCoord[0]][newCoord[1]] in ['.','E'] and newCoord not in dicoParcours:
                    dicoParcours[newCoord] = acc
                    recursivite(newCoord, acc+1)
    recursivite(start)
    return dicoParcours

def findCheats(dicoParcours):
    allCheatSavings = []
    for case in dicoParcours.keys():
        caseX,caseY = case
        for direction in DirectionType:
            addX,addY = direction.value
            newCoord = (caseX+addX*2,caseY+addY*2)
            if newCoord in dicoParcours:
                cheatSaving = dicoParcours[newCoord]-dicoParcours[case]-2
                if cheatSaving > 0: allCheatSavings.append(cheatSaving)
                #print(f"{case} -> {newCoord}")    
    return allCheatSavings

def main(chemin):
    labyrinthe = splitFile("\n",readFile(chemin))
    start = searchUniqELT(labyrinthe,"S")
    end = searchUniqELT(labyrinthe,"E")
    #print(start,end)
    dicoParcours = parcoursPath(labyrinthe,start,end)
    #print(dicoParcours)
    allCheatSavings = findCheats(dicoParcours)
    nbCheatSavingMore100 = 0
    for cheat in allCheatSavings:
        if cheat >= 100: nbCheatSavingMore100 += 1
    return nbCheatSavingMore100
    

print(main("datas/2024_day20_data"))
print(main("datas/2024_day20_exemple"))
