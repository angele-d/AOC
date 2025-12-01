
import sys
sys.setrecursionlimit(10000)

fichier = open("datas/2024_day6_data","r")

lignes = fichier.readlines()

for i in range (len(lignes)-1):
    lignes[i] = lignes[i][:-1]

def find_guard(lignes):
    for i in range (len(lignes)):
        ligne = lignes[i]
        if "^" in ligne or "v" in ligne or ">" in ligne or "<" in ligne:
            for j in range (len(ligne)):
               if ligne[j] in [">","<","^","v"]:
                   return (i,j)
    print("Problème dans find_guard") #problème

def dico_hashtag(lignes):
    dico = {}
    for i in range (len(lignes)):
        for j in range (len(lignes)):
            if lignes[i][j] == "#":
                dico[(i,j)] = "#"
    return dico

def est_dans_tableau(pos):
    if pos[0] < 0 or pos[0] >= len(lignes):
        return False
    else:
        if pos[1] < 0 or pos[1] >= len(lignes[pos[0]]):
            return False
        else:
            return True

def creer_tab_vide():
    tab_vide = [0] * len(lignes)
    for i in range (len(tab_vide)):
        tab_vide[i] = [0] * len(lignes[0])
    return tab_vide

def moove(pos_guard,direction_guard,dico_diese, acc = creer_tab_vide()):
    if not est_dans_tableau(pos_guard):
        return 0
    else:
        parcouru = acc[pos_guard[0]][pos_guard[1]]
        if parcouru == 0:
            acc[pos_guard[0]][pos_guard[1]] = 1
            score = 1
        else:
            score = 0
        match direction_guard:
            case ">":
                next = dico_diese.get((pos_guard[0],pos_guard[1]+1))
                if next == None: #tout droit
                    pos_guard = (pos_guard[0],pos_guard[1]+1)
                else: #diese ensuite 
                    pos_guard = (pos_guard[0]+1,pos_guard[1])
                    direction_guard = "v"
                return score + moove(pos_guard,direction_guard,dico_diese,acc)
            case "<":
                next = dico_diese.get((pos_guard[0],pos_guard[1]-1))
                if next == None: #tout droit
                    pos_guard = (pos_guard[0],pos_guard[1]-1)
                else: #diese ensuite 
                    pos_guard = (pos_guard[0]-1,pos_guard[1])
                    direction_guard = "^"
                return score + moove(pos_guard,direction_guard,dico_diese,acc)
            case "^":
                next = dico_diese.get((pos_guard[0]-1,pos_guard[1]))
                if next == None: #tout droit
                    pos_guard = (pos_guard[0]-1,pos_guard[1])
                else: #diese ensuite 
                    pos_guard = (pos_guard[0],pos_guard[1]+1)
                    direction_guard = ">"
                return score + moove(pos_guard,direction_guard,dico_diese,acc)
            case "v":
                next = dico_diese.get((pos_guard[0]+1,pos_guard[1]))
                if next == None: #tout droit
                    pos_guard = (pos_guard[0]+1,pos_guard[1])
                else: #diese ensuite 
                    pos_guard = (pos_guard[0],pos_guard[1]-1)
                    direction_guard = "<"
                return score + moove(pos_guard,direction_guard,dico_diese,acc)
            case _:
                print("Pb moove")

def init_search(lignes):
    pos_guard = find_guard(lignes)
    direction_guard = lignes[pos_guard[0]][pos_guard[1]]
    dico_diese = dico_hashtag(lignes)
    return moove(pos_guard,direction_guard,dico_diese)

print(init_search(lignes))