import sys
from enum import Enum
import math
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

def dist(case,newCoord):
    '''Distance entre coord de case et coord de newCoord'''
    distX = abs(newCoord[0]-case[0])
    distY = abs(newCoord[1]-case[1])
    return distX + distY

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
        for i in range (-20,21):
            for j in range (-20+abs(i),21-abs(i)):
                newCoord = (caseX+i,caseY+j)
                if newCoord in dicoParcours:
                    tailleCheat = dist(case,newCoord)
                    cheatSaving = dicoParcours[newCoord]-dicoParcours[case]-tailleCheat
                    if cheatSaving >= 100:
                        allCheatSavings.append(cheatSaving)
    return allCheatSavings

def studyExemple(tab):
    dico = {}
    for elt in tab:
        if elt in dico:
            dico[elt] = dico[elt]+1
        else:
            dico[elt] = 1
    print(dico)

def main(chemin):
    labyrinthe = splitFile("\n",readFile(chemin))
    start = searchUniqELT(labyrinthe,"S")
    end = searchUniqELT(labyrinthe,"E")
    #print(start,end)
    dicoParcours = parcoursPath(labyrinthe,start,end)
    #print(dicoParcours)
    allCheatSavings = findCheats(dicoParcours)
    print(allCheatSavings)
    studyExemple(allCheatSavings)
    return len(allCheatSavings)
    

print(main("datas/2024_day20_data"))
#print(main("datas/2024_day20_exemple")) #285 au dessus de 50
