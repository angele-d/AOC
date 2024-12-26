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

def findConnectionsWithT(connectionsOf3):
    goodSetsOf3 = []
    for connection in connectionsOf3:
        containsT = False
        for computer in connection:
            if computer[0] == 't': containsT = True
        if containsT: goodSetsOf3.append(connection)
    return goodSetsOf3

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

def main(chemin):
    network = splitFile("\n",readFile(chemin))
    allConnections = makeConnection(network)
    all2Connections = find2Connections(allConnections)
    connectionsWithT = findConnectionsWithT(all2Connections)
    return len(connectionsWithT)

print(main("datas/2024_day23_data"))