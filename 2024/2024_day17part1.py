import sys

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
    

#-------------#

comboOperands = {0:0,1:1,2:2,3:3,4:'A',5:'B',6:'C',7:'Probleme'}

def adv(Operand : int):
    numerateur = dicRegisters["A"]
    value = comboOperands[Operand]
    if type(value) == int: denominateur = 2**value
    elif len(value) == 1 : denominateur = 2**dicRegisters[value]
    else: print("Probleme adv")
    dicRegisters['A'] = numerateur//denominateur

def bxl(Operand : int):
    dicRegisters["B"] = dicRegisters["B"]^Operand

def bst(Operand : int):
    value = comboOperands[Operand]
    if type(value) == int: calcul = value%8
    elif len(value) == 1 : calcul = dicRegisters[value]%8
    else: print("Probleme bst")
    dicRegisters["B"] = calcul

def jnz(Operand : int) -> int:
    if dicRegisters["A"] == 0: return -1
    else: return Operand

def bxc(Operand : int):
    dicRegisters["B"] = dicRegisters["B"]^dicRegisters["C"]

def out(Operand : int):
    value = comboOperands[Operand]
    if type(value) == int: calcul = value%8
    elif len(value) == 1 : calcul = dicRegisters[value]%8
    else: print("Probleme out")
    strcalcul = str(calcul)
    reponse = strcalcul[0]
    for i in range (1,len(strcalcul)):
        reponse += ","
        reponse += strcalcul[i]
    #print(f"reponse_out: {reponse}")
    return reponse

def bdv(Operand : int):
    numerateur = dicRegisters["A"]
    value = comboOperands[Operand]
    if type(value) == int: denominateur = 2**value
    elif len(value) == 1 : denominateur = 2**dicRegisters[value]
    else: print("Probleme adv")
    dicRegisters['B'] = numerateur//denominateur

def cdv(Operand : int):
    numerateur = dicRegisters["A"]
    value = comboOperands[Operand]
    if type(value) == int: denominateur = 2**value
    elif len(value) == 1 : denominateur = 2**dicRegisters[value]
    else: print("Probleme adv")
    dicRegisters['C'] = numerateur//denominateur

def parcoursOutput(program):
    taille = len(program)
    i = 0
    result = ''
    while i < taille-1:
        opcode = program[i]
        operand = program[i+1]
        match opcode:
            case 0: 
                adv(operand)
                i += 2
            case 1: 
                bxl(operand)
                i += 2
            case 2: 
                bst(operand)
                i += 2
            case 3:
                jump = jnz(operand)
                if jump != -1: i = jump
                else: i += 2
            case 4:
                bxc(operand)
                i += 2
            case 5:
                result += out(operand) + ","
                i += 2
            case 6:
                bdv(operand)
                i += 2
            case 7:
                cdv(operand)
                i += 2
    return result[:-1]


#Part1
#chemin = "datas/2024_day17_exemple"
chemin = "datas/2024_day17_data"
registers,program = splitWhenEmptyLine(splitFile("\n",readFile(chemin)))
program = tabInt(splitFile(",",(program[0].split(": ")[1])))
A = int(registers[0].split(": ")[1])
B = int(registers[1].split(": ")[1])
C = int(registers[2].split(": ")[1])
dicRegisters = {"A":A,"B":B,"C":C}
print(parcoursOutput(program))
    

