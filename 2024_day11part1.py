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


#---------------------------#

def parcours_arrangement(arrangement):
    new_arrangement = []
    for tabNumber in arrangement:
        if len(tabNumber) == 1 and tabNumber[0] == 0: new_arrangement.append([1])
        elif est_pair(tabNumber):
            mid = len(tabNumber)//2
            new_arrangement.append(tabNumber[:mid]) #part1
            part2 = removeFront0(tabNumber[mid:])
            new_arrangement.append(part2)
        else:
            number = translationTabnumberNumber(tabNumber)
            number = number * 2024
            new_arrangement.append(translationNumberTabnumber(number))
    return new_arrangement


def main(chemin):
    arrangement = tableInt(returnLines(splitFile(" ",readFile(chemin))))
    #arrangement = tableInt(returnLines(splitFile(" ","125 17"))) #exemple
    for _ in range (25):
        arrangement = parcours_arrangement(arrangement)
    print(len(arrangement))

main("datas/2024_day11_data")