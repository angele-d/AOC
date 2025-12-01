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

#----------------------------#
keys = []
locks = []

def isFitting(keys,locks):
    nbFit = 0
    for lock in locks:
        for key in keys:
            i = 0
            while i < 5 and key[i] + lock[i] < 6:
                i += 1
            if i == 5: nbFit += 1
    return nbFit

def convertingLocksKeys(contenu):
    for patern in contenu:
        heights = []
        for j in range (len(patern[0])):
            i = 0
            while i < len(patern) and patern[i][j] == patern[0][0]:
                i += 1
            heights.append(i-1)
        match patern[0][0]:
            case "#": #lock
                locks.append(heights)
            case ".": #keys
                trueHeights = [5-heights[i] for i in range (len(heights))]
                keys.append(trueHeights)
            case _:
                print("Probleme convertingLocksKeys")
            
def main(chemin):
    contenu = splitWhenEmptyLine(splitFile("\n",readFile(chemin)))
    convertingLocksKeys(contenu)
    return isFitting(keys,locks)

#print(main("datas/2024_day25_exemple"))
print(main("datas/2024_day25_data"))