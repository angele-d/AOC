import sys
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

def tabInt(tab: list[str]):
    '''Passe les elts de tab en type int'''
    return [int(elt) for elt in tab]

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

#--------------------#

def find2000SecretNumber(number):
    unitNumber = []
    diffUnitNumber = []
    for _ in range (2000):
        step1 = ((number*64)^number)%16777216
        step2 = ((step1//32)^step1)%16777216
        step3 = ((step2*2048)^step2)%16777216
        if diffUnitNumber == []: diffUnitNumber.append(step3%10-number%10)
        else: diffUnitNumber.append(step3%10-unitNumber[-1])
        unitNumber.append(step3%10)
        number = step3
    return unitNumber,diffUnitNumber

def matchBestSequence(bestSequence,unitNumber,diffUnitNumber):
    i = 0
    while i < len(unitNumber)-3:
        if diffUnitNumber[i:i+4] == bestSequence:
            return unitNumber[i+3]
        i += 1
    return 0


def main(chemin):
    initialSecretNumber = tabInt(splitFile("\n",readFile(chemin)))
    #initialSecretNumber = [1,2,3,2024] #EXEMPLE
    allUnitNumber = []
    allDiffUnitNumber = []
    for initialNumber in initialSecretNumber:
        unitNumber,diffUnitNumber = find2000SecretNumber(initialNumber)
        allUnitNumber.append(unitNumber)
        allDiffUnitNumber.append(diffUnitNumber)
    mostOfAllbananas = 0
    for i in range (len(allUnitNumber)):
        for k in range (len(allUnitNumber[i])-3):
            mostBananas = 0
            bestSequence = allDiffUnitNumber[i][k:k+4]
            for j in range (i,len(allUnitNumber)):
                bananaGain = matchBestSequence(bestSequence,allUnitNumber[j],allDiffUnitNumber[j])
                mostBananas += bananaGain
            if mostBananas > mostOfAllbananas:
                mostOfAllbananas = mostBananas
    return mostOfAllbananas
    

print(main("datas/2024_day22_data"))