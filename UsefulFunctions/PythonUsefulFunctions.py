import sys
import itertools
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

def returnLineinTab(contenu: str) -> list[str]:
    '''Renvoie la ligne du fichier sous forme de tab'''
    line = [elt for elt in contenu]
    return line

def tabInt(tab: list[str]):
    '''Passe les elts de tab en type int'''
    return [int(elt) for elt in tab]

#-----------------#

def isInTable(table,coord):
    '''Verifie si les coord sont bien dans table et renvoie la valeur'''
    if (0 <= coord[0] < len(table)) and (0 <= coord[1] < len(table[coord[0]])):
        return table[coord[0]][coord[1]]
    else: return None

def isInTableByLen(coord:tuple[int,int],xmax:int,ymax:int) -> bool:
    '''Renvoie True/False selon presence d'une coord dans l'espace 0:xmax et 0:ymax'''
    if (0 <= coord[0] <= xmax) and (0 <= coord[1] <= ymax):
        return True 
    else: return False

def searchAround(table,coord):
    '''Renvoie valeur_coord[haut,droite,bas,gauche] de coord'''
    x,y = coord
    haut = isInTable(table,(x-1,y))
    droite = isInTable(table,(x,y+1))
    bas = isInTable(table,(x+1,y))
    gauche = isInTable(table,(x,y-1))
    return [haut,droite,bas,gauche]

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

def findMinInTab(tab,ANePasPrendreEnCompte):
    '''Renvoie le min dans un tableau tab, sans prendre en compte certains termes
    >>> findMinInTab([2,-1,1,6],[-1])
    1
    '''
    min = sys.maxsize
    for elt in tab:
        if elt not in ANePasPrendreEnCompte and elt < min:
            min = elt
    return min

def findMaxInTab(tab,ANePasPrendreEnCompte):
    '''Renvoie le max dans un tableau tab, sans prendre en compte certains termes
    >>> findMaxInTab([2,-1,1,6],[-1])
    6
    '''
    max = -sys.maxsize
    for elt in tab:
        if elt not in ANePasPrendreEnCompte and elt > max:
            max = elt
    return max

def concatene2TabStr(tab1,tab2):
    '''Concatene 2 tableau de str'''
    newTab = []
    for chaine1 in tab1:
        for chaine2 in tab2:
            newTab.append(chaine1+chaine2)
    return newTab

def checkDoublons(tab,ensemble):
    '''ensemble = tableau de plein d'elements
    on veut qu'1 permutation dans le tab final
    Renvoie le nombre de doublons'''
    nombreDoublons = 0
    permutations = list(itertools.permutations(ensemble))
    for permutation in permutations:
        if permutation in tab:
            nombreDoublons += 1
    return nombreDoublons

def dist(coord1,coord2):
    '''Distance entre coord1 et coord2'''
    distX = abs(coord2[0]-coord1[0])
    distY = abs(coord2[1]-coord1[1])
    return distX + distY

def distXY(coord1,coord2):
    '''Distance entre X de coord1 et coord2
    et Distance entre Y de coord1 et coord2 '''
    distX = abs(coord2[0]-coord1[0])
    distY = abs(coord2[1]-coord1[1])
    return distX,distY

def searchUniqELT(table,elt):
    '''Trouve l'elt dans la table'''
    for i in range (len(table)):
        for j in range (len(table[i])):
            if table[i][j] == elt:
                return i,j
    return None

def digits_count(n : int) -> int:
    '''Renvoie le nombre de chiffre d'un entier n'''
    if n == 0: return 1
    d = 0
    while n > 0:
        d += 1
        n = n // 10
    return d

def estPairNbChiffre(n : int) -> bool:
    '''Verifie si un entier n a un nombre pair de chiffres'''
    return digits_count(n) % 2 == 0

def split_int(n: int) -> tuple[int, int]:
    '''Casser un entier en 2 entiers selon leur nombre de chiffres
    >>> split_int(2452)
    24,52
    '''
    d = digits_count(n) // 2
    p = 10**d
    left = n // p
    right = n % p 
    return left, right

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
    return distStart[endCoord]    