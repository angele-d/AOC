
fichier = open("datas/2024_day5_data","r")

lignes = fichier.readlines()

indice_vide = lignes.index("\n")
rules = lignes[:indice_vide]
for i in range (len(rules)):
    rules[i] = rules[i][:-1]
updates = lignes[indice_vide+1:]

updatestab = []
for i in range (len(updates)):
    updates[i] = updates[i][:-1]
    splitter = updates[i].split(",")
    updatestab.append(splitter)


def est_bon(rules,update):
    for i in range (len(update)):
        avant = []
        apres = []
        for j in range (len(rules)):
            if update[i] in rules[j]:
                if rules[j].index(update[i]) < rules[j].index("|"):
                    if rules[j][3:5] in update:
                        apres.append(int(rules[j][3:5]))
                elif rules[j].index(update[i]) > rules[j].index("|"):
                    if rules[j][0:2] in update:
                        avant.append(int(rules[j][0:2]))
        print(f"{update[i]}: {avant} {apres}")
        for find in avant:
            index_before = update.index(str(find))
            if index_before > i:
                return False
        for find in apres:
            index_after = update.index(str(find))
            if index_after < i:
                return False   
    return True     

def recherche_bon_update(rules,updates):
    bon_update = []
    for update in updates:
        if est_bon(rules,update):
            bon_update.append(update)
        print("\n")
    return bon_update
    
def middle_search_bon_update(rules,updates):
    bon_update = recherche_bon_update(rules,updates)
    somme = 0
    for update in bon_update:
        imilieu = len(update)//2
        print(update[imilieu])
        somme += int(update[imilieu])
    return somme


print(middle_search_bon_update(rules,updatestab))

