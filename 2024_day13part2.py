
import re #Pour regex
import sympy as sy #Resoudre 2 equations a 2 inconnues


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


def studyMachine(machine):
    dataMachine = []
    for info in machine:
        datas = re.findall(r'\w+\s*\w*:\sX[\+=](\d+),\sY[\+=](\d+)',info)
        dataMachine.append(datas[0])
    dataMachine = tableInt(dataMachine)
    dataMachine[2][0] = dataMachine[2][0] + 10000000000000
    dataMachine[2][1] = dataMachine[2][1] + 10000000000000
    #Debut etude
    a = sy.Symbol("a")
    b = sy.Symbol("b")
    eq1 = sy.Eq(a*dataMachine[0][0]+b*dataMachine[1][0], dataMachine[2][0])
    eq2 = sy.Eq(a*dataMachine[0][1]+b*dataMachine[1][1], dataMachine[2][1])
    solution = sy.solve((eq1,eq2),(a,b))
    if solution[a] == int(solution[a]) and solution[b] == int(solution[b]):
        tokensA = solution[a]*3
        tokensB = solution[b]*1
        return tokensA+tokensB
    else: return 0

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

