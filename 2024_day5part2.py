
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
for i in range (len(updates)):
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
        for find in avant:
            index_before = update.index(str(find))
            if index_before > i:
                return False
        for find in apres:
            index_after = update.index(str(find))
            if index_after < i:
                return False   
    return True     

def recherche_pas_bon_update(rules,updates):
    pas_bon_update = []
    for update in updates:
        if not est_bon(rules,update):
            pas_bon_update.append(update)
    #print(f"rpbu: {pas_bon_update}")
    return pas_bon_update

def modif_middle(rules,pas_bon_update):
    new_tab = [0] * len(pas_bon_update)
    #print(pas_bon_update)
    for i in range (len(pas_bon_update)):
        avant = []
        apres = []
        for j in range (len(rules)):
            if pas_bon_update[i] in rules[j]:
                if rules[j].index(pas_bon_update[i]) < rules[j].index("|"):
                    if rules[j][3:5] in pas_bon_update:
                        apres.append(int(rules[j][3:5]))
                elif rules[j].index(pas_bon_update[i]) > rules[j].index("|"):
                    if rules[j][0:2] in pas_bon_update:
                        avant.append(int(rules[j][0:2]))
        new_tab[len(avant)] = pas_bon_update[i]
    print(new_tab)
    return new_tab   

def middle_search_pas_bon_update(rules,updates):
    pas_bon_updates = recherche_pas_bon_update(rules,updates)
    somme = 0
    for pas_bon_update in pas_bon_updates:
        #print(f"mspbu: {pas_bon_update}")
        new_update = modif_middle(rules,pas_bon_update)
        imilieu = len(new_update)//2
        #print(new_update[imilieu])
        somme += int(new_update[imilieu])
    return somme


print(middle_search_pas_bon_update(rules,updatestab))

