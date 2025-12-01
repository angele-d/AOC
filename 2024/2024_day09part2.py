import sys
sys.setrecursionlimit(10000)

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

def returnLineinTab(contenu: str) -> list[str]:
    '''Renvoie la ligne du fichier sous forme de tab'''
    line = [elt for elt in contenu]
    return line

def tableInt(table):
    '''Passe les elts de table en type int'''
    new_table = []
    for i in range (len(table)):
        new_table.append([int(elt) for elt in table[i]])
    return new_table

def tabInt(tab: list[str]):
    '''Passe les elts de tab en type int'''
    return [int(elt) for elt in tab]

#------------------------------------------#

def translateDiskmap(diskmap):
    dico = {} #id: taille
    id = 0
    is_file = 1
    filesystem = []
    while diskmap != []:
        if is_file:
            dico[id] = diskmap[0]
            for _ in range (diskmap[0]):
                filesystem.append(str(id))
            id += 1
        else:
            for _ in range (diskmap[0]):
                filesystem.append(".")
        is_file = 1-is_file
        diskmap = diskmap[1:]
    return dico,filesystem

def firstTrou(filesystem) -> (int,int):
    '''Trouve le 1er trou et renvoie sa coordonnee et la quantite de trous a la suite'''
    for i in range (len(filesystem)):
        if filesystem[i] == ".":
            j = i
            while j < len(filesystem) and filesystem[j] == ".":
                j += 1
            return i,j-i
    return -1,-1

def existTrou(filesystem,tailleMinTrou,maxIndice):
    for i in range (maxIndice):
        if filesystem[i] == ".":
            j = 0
            while i+j < len(filesystem) and filesystem[i+j] == ".":
                if tailleMinTrou <= j+1: return i
                else: j += 1
    return -1

def comblerTrousStrategique(filesystem,relationIdTaille):
    j = len(filesystem)-1
    while j >= 0:
        while filesystem[j] == ".": j -= 1
        id = filesystem[j]
        tailleId = relationIdTaille[int(id)]
        coordTrou = existTrou(filesystem,tailleId,j)
        if coordTrou != -1 and coordTrou < j: #existe un trou qui convient
            for k in range (0,tailleId):
                filesystem[coordTrou+k] = id
                filesystem[j-k] = "."
        else:
            j -= tailleId
    return filesystem

def calculChecksum(filesystemFull):
    somme = 0
    for i in range (len(filesystemFull)):
        if filesystemFull[i] != ".":
            somme += i * int(filesystemFull[i])
    return somme

def main(chemin):
    line = tabInt(returnLineinTab(splitFile("\n",readFile(chemin))))
    relationIdTaille,filesystem = translateDiskmap(line)
    filesystemFull = comblerTrousStrategique(filesystem,relationIdTaille)
    return calculChecksum(filesystemFull)


print(main("datas/2024_day9_exemple"))
print(main("datas/2024_day9_data"))
