import sys
from enum import Enum
sys.setrecursionlimit(10000)
import functools

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

def concatene2TabStr(tab1,tab2):
    '''Concatene 2 tableau de str'''
    newTab = []
    for chaine1 in tab1:
        for chaine2 in tab2:
            newTab.append(chaine1+chaine2)
    return newTab

def distXY(coord1,coord2):
    '''Distance entre X de coord1 et coord2
    et Distance entre Y de coord1 et coord2 '''
    distX = coord2[0]-coord1[0]
    distY = coord2[1]-coord1[1]
    return distX,distY

#-------------------------#

dicNumericPad = {'A':(3,2),'0':(3,1),'1':(2,0),'2':(2,1),'3':(2,2),
'4':(1,0),'5':(1,1),'6':(1,2),'7':(0,0),'8':(0,1),'9':(0,2),'F':(3,0)}
#F = forbidden
dicDirectionalPad = {'A':(0,2),"^":(0,1),"v":(1,1),
                    "<":(1,0),">":(1,2),'F':(0,0)}

@functools.cache
def allPaths(pointA,pointB,without):
    '''de pointA à pointB sans passer par without
    Principe: trouve 1 chemin; puis permutations des elements'''
    distX,distY = distXY(pointA,pointB)
    onePath = ''
    if distX <= 0: #pointB au dessus de pointA
        onePath = onePath + '^'*abs(distX)
    else:
        onePath = onePath + 'v'*abs(distX)
    if distY <= 0: #pointB à gauche de pointA
        onePath = onePath + '<'*abs(distY)
    else: 
        onePath = onePath + '>'*abs(distY)

    allPermutations = [onePath]
    def generatePermutation(prefix,remaining):
        if remaining == '': 
            if prefix not in allPermutations:
                allPermutations.append(prefix)
        else:
            for i in range (len(remaining)):
                generatePermutation(prefix + remaining[i],remaining[:i]+remaining[i+1:])
    generatePermutation("",onePath)

    #Verifie si on passe par case vide:
    if without[0] in [pointA[0],pointB[0]] and without[1] in [pointA[1],pointB[1]]:
        match without:
            case (3,0): #sur numericPad
                if "v"*abs(distX) + ">"*abs(distY) in allPermutations:
                    del allPermutations[allPermutations.index("v"*abs(distX) + ">"*abs(distY))]
                if "<"*abs(distY) + "^"*abs(distX) in allPermutations:
                    del allPermutations[allPermutations.index("<"*abs(distY) + "^"*abs(distX))]
            case (0,0): #sur directionnalPad   
                if "^"*abs(distX) + ">"*abs(distY) in allPermutations:
                    del allPermutations[allPermutations.index("^"*abs(distX) + ">"*abs(distY))]
                if "<"*abs(distY) + "v"*abs(distX) in allPermutations:
                    del allPermutations[allPermutations.index("<"*abs(distY) + "v"*abs(distX))]
    return allPermutations


def moveNumericPad(code,previousButton = dicNumericPad['A']):
    if code == '': return ['']
    else:
        button = code[0]
        coordButton = dicNumericPad[button]
        paths = allPaths(previousButton,coordButton,dicNumericPad['F'])
        nextSequences = moveNumericPad(code[1:],coordButton)
        concatpathsA = concatene2TabStr(paths,['A'])
        return concatene2TabStr(concatpathsA,nextSequences)

@functools.cache
def moveDirectionalPad(code,previousButton = dicDirectionalPad['A']):
    if code == '': return ['']
    else:
        button = code[0]
        coordButton = dicDirectionalPad[button]
        paths = allPaths(previousButton,coordButton,dicDirectionalPad['F'])
        nextSequences = moveDirectionalPad(code[1:],coordButton)
        concatpathsA = concatene2TabStr(paths,['A'])
        return concatene2TabStr(concatpathsA,nextSequences)

def findShortest(allMove):
    minlen = (min(len(allMove[i]) for i in range (len(allMove))))
    returnMove = []
    for move in allMove:
        if len(move) == minlen and move not in returnMove:
            returnMove.append(move)
    return returnMove

def main(chemin):
    fiveCodes = splitFile("\n",readFile(chemin))
    lenFiveCodes = []
    for code in fiveCodes:
        move1 = moveNumericPad(code)
        shortMove1 = findShortest(move1)
        allMoves2 = []
        for code1 in shortMove1:
            allMoves2 = allMoves2 + moveDirectionalPad(code1)
        shortMove2 = findShortest(allMoves2)
        allMoves3 = []
        for code2 in shortMove2:
            allMoves3 = allMoves3+ moveDirectionalPad(code2)
        #shortMove3 = findShortest(allMoves3)
        lenFiveCodes.append(min(len(mv) for mv in allMoves3))
    
    somme = 0
    for i in range (len(fiveCodes)):
        fact = int(fiveCodes[i][:-1])*lenFiveCodes[i]
        somme += fact
    return somme

print(main("datas/2024_day21_data"))
#print(main("datas/2024_day21_exemple"))
