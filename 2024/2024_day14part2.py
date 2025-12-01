import re

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

#--------------#

def stayIn(coord):
    x,y = coord
    if 0 > x:
        x = xmax+x
    elif x >= xmax:
        x = x-xmax
    if 0 > y:
        y = ymax+y
    elif y >= ymax:
        y = y-ymax
    return x,y

def movement(infosRobots):
    nextMove = {}
    keys = list(infosRobots.keys())
    values = list(infosRobots.values())
    for i in range (len(keys)):
        key = keys[i]
        value = values[i]
        if value != None:
            for velocityRobot in value:
                newX = key[0] + velocityRobot[0]
                newY = key[1] + velocityRobot[1]
                newXY = stayIn((newX,newY))
                if nextMove.get(newXY) == None:
                    nextMove[newXY] = [velocityRobot]
                else:
                    nextMove[newXY].append(velocityRobot)
    return nextMove

def studyRobots(robots):
    transcriptionInfosRobots = {}
    for robot in robots:
        pos,velocite = robot.split(" ")
        pos = tuple(tableInt(re.findall(r'p\=(\d+),(\d+)',robot))[0])
        velocite = tuple(tableInt(re.findall(r'v\=(-?\d+),(-?\d+)',velocite))[0])
        if transcriptionInfosRobots.get(pos) == None:
            transcriptionInfosRobots[pos] = [velocite]
        else:
            transcriptionInfosRobots[pos].append(velocite)
        #print(f"Robot sur {pos}: {transcriptionInfosRobots[pos]}")
    return transcriptionInfosRobots

def affichage(infosRobots):
    tab = [0]*ymax
    for i in range (len(tab)):
        tab[i] = [0]*xmax
    keys = list(infosRobots.keys())
    values = list(infosRobots.values())
    for i in range (len(keys)):
        if values[i] != None:
            nbRobots = len(values[i])
            tab[keys[i][1]][keys[i][0]] = nbRobots
    for ligne in tab:
        print(ligne)
    print("\n")

def isChristmasTree(infosRobots):
    cles = infosRobots.keys()
    for cle in cles:
        x,y = cle
        #Cherche une colonne de + de 10robots a la suite
        ineg = 0
        ipos = 0
        while infosRobots.get((x-ineg,y)) != None:
            ineg += 1
        if ineg >= 10:
            return True
        while infosRobots.get((x+ipos,y)) != None:
            ipos += 1
        if ipos >= 10:
            return True
        if ineg+ipos >= 10:
            return True
        jneg = 0
        jpos = 0
        while infosRobots.get((x,y-jneg)) != None:
            jneg += 1
        if jneg >= 10:
            return True
        while infosRobots.get((x,y+jpos)) != None:
            jpos += 1
        if jpos >= 10:
            return True
        if jneg+jpos+1 >= 10:
            return True
    return False

def findQuarter(coord):
    x,y = coord
    xmid = xmax//2
    ymid = ymax//2
    if x < xmid and y < ymid: return 0 #haut gauche
    elif x > xmid and y < ymid: return 1 #haut droit
    elif x < xmid and y > ymid: return 2 #bas gauche
    elif x > xmid and y > ymid: return 3 #bas droit
    else: return 5 #au mid

def splitIntoQuarters(infosRobots):
    keys = list(infosRobots.keys())
    values = list(infosRobots.values())
    nbRobotsEachQuarter = [0,0,0,0]
    for i in range (len(keys)):
        quarter = findQuarter(keys[i])
        if quarter != 5 and values[i] != None:
            nbRobotsEachQuarter[quarter] = nbRobotsEachQuarter[quarter]+len(values[i])
    return nbRobotsEachQuarter

def main(chemin):
    global xmax
    global ymax
    xmax = 101 #101 / Ex: 11
    ymax = 103 #103 / Ex: 7
    contenu = splitFile("\n",readFile(chemin))
    infosRobots = studyRobots(contenu)
    for i in range (0,1000000):
        infosRobots = movement(infosRobots)
        if isChristmasTree(infosRobots):
            return i+1
    return -1


print(main("datas/2024_day14_data"))
#print(main("datas/2024_day14_exemple"))