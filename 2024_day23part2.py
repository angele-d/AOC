import itertools

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

def checkDoublons(tab,ensemble):
    '''ensemble = tableau de plein d'elements
    on veut qu'1 permutation dans le tab final
    Renvoie le nombre de doublons'''
    nombreDoublons = 0
    permutations = list(itertools.permutations(ensemble))
    for permutation in permutations:
        if permutation in tab:
            nombreDoublons += 1
    return nombreDoublons

#---------------------------#

def findMoreConnections(connectionsOf3):
    iMaxLan = 0
    computerILan = {}
    for triplet in connectionsOf3:
        if triplet[0] not in computerILan and triplet[1] not in computerILan and triplet[2] not in computerILan:
            for elt in triplet:
                computerILan[elt] = iMaxLan
            iMaxLan+=1
        else:
            if computerILan.get(triplet[0]) == computerILan.get(triplet[1]) != None:
                computerILan[triplet[2]] = computerILan.get(triplet[0])
            elif computerILan.get(triplet[0]) == computerILan.get(triplet[2]) != None:
                computerILan[triplet[1]] = computerILan.get(triplet[0])
            elif computerILan.get(triplet[2]) == computerILan.get(triplet[1]) != None:
                computerILan[triplet[0]] = computerILan.get(triplet[2])
            else:
                newParty = []
                for elt in triplet:
                    if elt not in computerILan: newParty.append(elt)
                if newParty != []: 
                    for elt in newParty: computerILan[elt] = iMaxLan
                iMaxLan+=1
    return computerILan

def find2Connections(connections):
    connectionsOf3 = []
    for computer in connections:
        if len(connections[computer]) >= 2:
            for i in range (len(connections[computer])):
                for j in range (i,len(connections[computer])):
                    c1 = connections[computer][i]
                    c2 = connections[computer][j]
                    if c1 in connections[c2]: #existe connection entre c1 et c2
                        if checkDoublons(connectionsOf3,[computer,c1,c2]) == 0:
                            connectionsOf3.append((computer,c1,c2))
    return connectionsOf3

def makeConnection(network):
    connections = {}
    for connection in network:
        c1,c2 = connection.split("-")
        if c1 in connections: connections[c1].append(c2)
        else: connections[c1] = [c2]
        if c2 in connections: connections[c2].append(c1)
        else: connections[c2] = [c1]
    return connections

def findTrueLAN(lanPartys : dict[str:int],allConnections) -> list[list[str]]:
    tabLanPartys = {}
    for computer in lanPartys:
        indice = lanPartys[computer]
        if indice in tabLanPartys: tabLanPartys[indice].append(computer)
        else: tabLanPartys[indice] = [computer]
    print(tabLanPartys)
    trueLan = []
    for indice in tabLanPartys:
        lan = tabLanPartys[indice]
        if len(lan) <= 2: pass
        else:
            isLAN = True
            for i in range (len(lan)-1):
                for j in range (i+1, len(lan)):
                    if not lan[j] in allConnections[lan[i]]: isLAN = False
            if isLAN: trueLan.append(lan)
    return trueLan

def returnInOrder(trueLan: list[str]):
    for i in range (len(trueLan)-1):
        iMinSTR = i
        for j in range (i+1,len(trueLan)):
            if trueLan[j] < trueLan[iMinSTR]:
                iMinSTR = j
        if iMinSTR != i:
            temp = trueLan[i]
            trueLan[i] = trueLan[iMinSTR]
            trueLan[iMinSTR] = temp
    print(trueLan)
    rep = ""
    for i in range (len(trueLan)-1):
        rep = rep + trueLan[i] + ","
    rep = rep + trueLan[-1]
    return rep

def main(chemin):
    network = splitFile("\n",readFile(chemin))
    allConnections = makeConnection(network)
    all2Connections = find2Connections(allConnections)
    lanPartys = findMoreConnections(all2Connections)
    trueLan = findTrueLAN(lanPartys,allConnections)
    return returnInOrder(trueLan[0])

print(main("datas/2024_day23_data"))
#print(main("datas/2024_day23_exemple"))
