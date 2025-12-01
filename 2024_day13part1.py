
import re


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

#--------------------#

def touchButton(buttonA,buttonB,prize):
    maxAX = min(prize[0]//buttonA[0],100)
    maxAY = min(prize[1]//buttonA[1],100)
    maxA = min(maxAX,maxAY)
    maxBX = min(prize[0]//buttonB[0],100)
    maxBY = min(prize[1]//buttonB[1],100)
    maxB = min(maxBX,maxBY)
    possibilites = []
    for numPlayedB in range (0,maxB+1):
        tempPrizeB = (numPlayedB*buttonB[0],numPlayedB*buttonB[1])
        for numPlayedA in range (0,maxA+1):
            tempPrizeA = (numPlayedA*buttonA[0],numPlayedA*buttonA[1])
            tempPrize = (tempPrizeA[0]+tempPrizeB[0],tempPrizeA[1]+tempPrizeB[1])
            #print(f"A:{numPlayedA}->{tempPrizeA} ; B:{numPlayedB}->{tempPrizeB}--->{tempPrize}")
            if tempPrize[0] == prize[0] and tempPrize[1] == prize[1]:
                possibilites.append((numPlayedA,numPlayedB))
    return possibilites

def cheapestPossibility(possibilities):
    tokenA = possibilities[0][0]*3
    tokenB = possibilities[0][1]*1
    token = tokenA + tokenB
    theCheapest = token,possibilities[0]
    for possibility in possibilities:
        tokenA = possibility[0]*3
        tokenB = possibility[1]*1
        token = tokenA + tokenB
        if token < theCheapest[0]:
            theCheapest = token,possibility
    return theCheapest

def studyMachine(machine):
    dataMachine = []
    for info in machine:
        datas = re.findall(r'\w+\s*\w*:\sX[\+=](\d+),\sY[\+=](\d+)',info)
        dataMachine.append(datas[0])
    dataMachine = tableInt(dataMachine)
    #Debut etude
    possibilities = touchButton(dataMachine[0],dataMachine[1],dataMachine[2])
    #print(dataMachine,possibilities)
    if possibilities != []:
        theCheapest = cheapestPossibility(possibilities)
        #print(theCheapest)
        return theCheapest[0]
    else:
        return 0

def main(chemin):
    contenu = splitFile("\n",readFile(chemin))
    machines = splitWhenEmptyLine(contenu)
    lowerCost = 0
    for machine in machines:
        lowCost = studyMachine(machine)
        lowerCost += lowCost
    return lowerCost

print(main("datas/2024_day13_data"))
#print(main("datas/2024_day13_exemple"))

