
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
    tab_vide = ['V'] * len(lignes)
    for i in range (len(tab_vide)):
        tab_vide[i] = ['V'] * len(lignes[i])
    return tab_vide

def boucle_possible(pos_guard,direction_guard,dico_diese,acc):
    match direction_guard:
        case ">":
            if (pos_guard[0],pos_guard[1]+1) == init_guard or not est_dans_tableau((pos_guard[0],pos_guard[1]+1)):
                return 0
            if est_dans_tableau((pos_guard[0]+2,pos_guard[1])):
                diese_ligne = 0
                for i in range (pos_guard[0]+2,len(lignes)):
                    if dico_diese.get((i,pos_guard[1])) == "#" and acc[i-1][pos_guard[1]] == "<":
                        diese_ligne += 1
                return diese_ligne
            else:
                return 0
        case "<":
            if (pos_guard[0],pos_guard[1]-1) == init_guard or not est_dans_tableau((pos_guard[0],pos_guard[1]-1)):
                return 0
            if est_dans_tableau((pos_guard[0]-2,pos_guard[1])):
                diese_ligne = 0
                for i in range (0,pos_guard[0]-1):
                    if dico_diese.get((i,pos_guard[1])) == "#" and acc[i+1][pos_guard[1]] == ">":
                        diese_ligne += 1
                return diese_ligne
            else:
                return 0
        case "^":
            if (pos_guard[0]-1,pos_guard[1]) == init_guard or not est_dans_tableau((pos_guard[0]-1,pos_guard[1])):
                return 0
            if est_dans_tableau((pos_guard[0],pos_guard[1]+2)):
                diese_ligne = 0
                for j in range (pos_guard[1]+2,len(lignes[pos_guard[0]])):
                    if dico_diese.get((pos_guard[0],j)) == "#" and acc[pos_guard[0]][j-1] == "v":
                        diese_ligne += 1
                return diese_ligne
            else:
                return 0
        case "v":
            if (pos_guard[0]+1,pos_guard[1]) == init_guard or not est_dans_tableau((pos_guard[0]+1,pos_guard[1])):
                return 0
            if est_dans_tableau((pos_guard[0],pos_guard[1]-2)):
                diese_ligne = 0
                for j in range (0,pos_guard[1]-1):
                    if dico_diese.get((pos_guard[0],j)) == "#" and acc[pos_guard[0]][j+1] == "^":
                        diese_ligne += 1
                return diese_ligne
            else:
                return 0
        case _:
            print("Pb deja_vu_droite")


def moove(pos_guard,direction_guard,dico_diese, acc = creer_tab_vide()):
    pos_init = pos_guard
    if not est_dans_tableau(pos_guard):
        return 0
    else:
        if boucle_possible(pos_guard,direction_guard,dico_diese,acc):
            score = 1
        else:
            score = 0
        match direction_guard:
            case ">":
                next = dico_diese.get((pos_guard[0],pos_guard[1]+1))
                if next == None: #tout droit
                    pos_guard = (pos_guard[0],pos_guard[1]+1)
                else: #diese ensuite 
                    pos_guard = (pos_guard[0],pos_guard[1])
                    score = 0
                    direction_guard = "v"
                acc[pos_init[0]][pos_init[1]] = direction_guard
                return score + moove(pos_guard,direction_guard,dico_diese,acc)
            case "<":
                next = dico_diese.get((pos_guard[0],pos_guard[1]-1))
                if next == None: #tout droit
                    pos_guard = (pos_guard[0],pos_guard[1]-1)
                else: #diese ensuite 
                    pos_guard = (pos_guard[0],pos_guard[1])
                    score = 0
                    direction_guard = "^"
                acc[pos_init[0]][pos_init[1]] = direction_guard
                return score + moove(pos_guard,direction_guard,dico_diese,acc)
            case "^":
                next = dico_diese.get((pos_guard[0]-1,pos_guard[1]))
                if next == None: #tout droit
                    pos_guard = (pos_guard[0]-1,pos_guard[1])
                else: #diese ensuite 
                    pos_guard = (pos_guard[0],pos_guard[1])
                    score = 0
                    direction_guard = ">"
                acc[pos_init[0]][pos_init[1]] = direction_guard
                return score + moove(pos_guard,direction_guard,dico_diese,acc)
            case "v":
                next = dico_diese.get((pos_guard[0]+1,pos_guard[1]))
                if next == None: #tout droit
                    pos_guard = (pos_guard[0]+1,pos_guard[1])
                else: #diese ensuite 
                    pos_guard = (pos_guard[0],pos_guard[1])
                    score = 0
                    direction_guard = "<"
                acc[pos_init[0]][pos_init[1]] = direction_guard
                return score + moove(pos_guard,direction_guard,dico_diese,acc)
            case _:
                print("Pb moove")

def init_search(lignes):
    global init_guard
    init_guard = find_guard(lignes)
    direction_guard = lignes[init_guard[0]][init_guard[1]]
    dico_diese = dico_hashtag(lignes)
    return moove(init_guard,direction_guard,dico_diese)


print(init_search(lignes))
