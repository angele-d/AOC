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

#--------------------#

def find2000SecretNumber(number):
    for i in range (2000):
        step1 = ((number*64)^number)%16777216
        step2 = ((step1//32)^step1)%16777216
        step3 = ((step2*2048)^step2)%16777216
        number = step3
    return number

def main(chemin):
    initialSecretNumber = tabInt(splitFile("\n",readFile(chemin)))
    secretNumber2000 = []
    for initialNumber in initialSecretNumber:
        secretNumber2000.append(find2000SecretNumber(initialNumber))
    somme = 0
    for number in secretNumber2000:
        somme += number
    return somme

print(main("datas/2024_day22_data"))