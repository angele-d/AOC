import functools
import sys
sys.setrecursionlimit(10000)


def readFile(chemin):
    '''Lecture d'un fichier'''
    fichier = open(chemin,"r")
    return fichier.read()

def splitFile(separateur: str,contenu):
    '''Split d'un fichier selon separateur'''
    splitter = contenu.split(separateur)
    if splitter[-1][-1] == "\n": #Retirer le \n a la fin du fichier
        splitter[-1] = splitter[-1][:-1]
    return splitter

def returnLines(contenu):
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

def tabInt(tab):
    '''Passe les elts de tab en type int'''
    return [int(elt) for elt in tab]

def est_pair(tabNumber):
    '''Verifie que la taille d'un tableau (de chiffre representant un nombre) est pair'''
    return len(tabNumber)%2 == 0

def removeFront0(tabNumber):
    '''Retire les 0 a l'avant d'un tableau representant un nombre'''
    i = 0
    while i < len(tabNumber) and tabNumber[i] == 0:
        i += 1
    if i == len(tabNumber): return [0] 
    else: return tabNumber[i:]

def translationTabnumberNumber(tabNumber):
    '''Traduit un tableau représentant un nombre en ce nombre'''
    nombre = 0
    for i in range (len(tabNumber)):
        nombre += tabNumber[i] * 10**(len(tabNumber)-i-1)
    return nombre

def translationNumberTabnumber(number):
    '''Traduit un nombre en un tableau le représentant'''
    strnumber = str(number)
    tabNumber = tabInt(list(strnumber))
    return tabNumber

def digits_count(n : int) -> int:
    '''Renvoie le nombre de chiffre d'un entier n'''
    if n == 0: return 1
    d = 0
    while n > 0:
        d += 1
        n = n // 10
    return d

def est_pair_num(n : int) -> bool:
    '''Verifie si un entier n a un nombre pair de chiffres'''
    return digits_count(n) % 2 == 0

def split_int(n: int) -> tuple[int, int]:
    '''Casser un entier en 2 entiers selon leur nombre de chiffres'''
    d = digits_count(n) // 2
    p = 10**d
    left = n // p
    right = n % p 
    return left, right

#---------------------------#

@functools.cache
def parcours_arrangement(number, nb_blinks):
    if nb_blinks == 0:
        return 1
    else:
        if number == 0: return parcours_arrangement(1,nb_blinks-1)
        elif est_pair_num(number):
            number1, number2 = split_int(number)
            arrangementPart1 = parcours_arrangement(number1,nb_blinks-1)
            arrangementPart2 = parcours_arrangement(number2,nb_blinks-1)
            return arrangementPart1 + arrangementPart2
        else:
            number = number * 2024
            return parcours_arrangement(number,nb_blinks-1)


def main(chemin,nb_blinks):
    arrangement = tabInt(splitFile(" ",readFile(chemin)))
    #arrangement = tabInt(returnLines(splitFile(" ","125 17"))) #exemple
    finalArrangement = 0
    for number in arrangement:
        finalArrangement = finalArrangement + parcours_arrangement(number,nb_blinks)
    print(finalArrangement)



main("datas/2024_day11_data",75)
