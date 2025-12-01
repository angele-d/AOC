from enum import Enum

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



def parcoursConnections(wires):
    keys = sorted(wires)[::-1]
    remainingWires = {}
    for key in keys:
        #print(key)
        g1,g2,result = key
        if g1 in dicOutput and g2 in dicOutput:
            #print(f"IN Output --> {wires[key]}")
            operator = wires[key]
            match operator:
                case "OR": dicOutput[result] = (dicOutput[g1] or dicOutput[g2])
                case "AND": dicOutput[result] = (dicOutput[g1] and dicOutput[g2])
                case "XOR": dicOutput[result] = (dicOutput[g1] != dicOutput[g2])
        else:
            remainingWires[key] = wires[key]
            #print(f"OUT output -> {remainingWires}")
    #print(remainingWires)
    if remainingWires != {}: parcoursConnections(remainingWires)
    
def produceNumber():
    keys = sorted(dicOutput)[::-1]
    dicOfZ = {}
    i = 0
    while keys[i][0] == 'z':
        dicOfZ[keys[i]] = dicOutput[keys[i]]
        i += 1
    number = 0
    for key in dicOfZ:
        number += dicOfZ[key]*2**(int((key[1:])))
    return number

def main(chemin):
    global dicOutput
    wires,connections = splitWhenEmptyLine(splitFile("\n",readFile(chemin)))
    dicOutput = {}
    for wire in wires:
        w,booleen = wire.split(": ")
        dicOutput[w] = int(booleen)
    wires = {}
    for connection in connections:
        calcul,result = connection.split(" -> ")
        calcul = calcul.split(" ")
        wires[(calcul[0],calcul[2],result)] = calcul[1]
    parcoursConnections(wires)
    number = produceNumber()
    return number

#print(main("datas/2024_day24_exemple1"))
print(main("datas/2024_day24_data"))

#Pour part2: je n'ai absolument rien compris à comment faire
#donc pas de code pour la part2 fait par moi-même