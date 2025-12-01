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

#---------------------#

@functools.cache
def nbPossibleDesign(design):
    #print(f"Current design: {design}")
    if design == '': return 1
    else: 
        nbDiffWays = 0
        for possible in available:
            lenPossible = len(possible)
            #print(f"Available {possible}: len={lenPossible}")
            if design[:lenPossible] == possible:
                #print(f"isOK {possible}")
                nbDiffWays += nbPossibleDesign(design[lenPossible:])
        return nbDiffWays


def main(chemin):
    global available
    all = splitWhenEmptyLine(splitFile("\n",readFile(chemin)))
    available = splitFile(", ",all[0][0])
    designs = all[1]
    available = sorted(available)[::-1]
    nbPossibleDesigns = 0
    for design in designs:
        nbPossibleDesigns += nbPossibleDesign(design)
    return nbPossibleDesigns
    
    

print(main("datas/2024_day19_data"))
#print(main("datas/2024_day19_exemple"))