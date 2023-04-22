#!/usr/bin/env python3
def OuExclusif(valeur_one, valeur_two):
    interact = ""
    tableau_k = ["" for i in range(len(valeur_one))]
    for i in range(len(valeur_one)):
        variable_one = valeur_one[i:i + 1]
        variable_two = valeur_two[i:i + 1]
        tableau_k[i] = "0" if variable_one == variable_two else "1"
    for i in tableau_k:
        interact += i
    return interact

def OuLogique(valeur_one, valeur_two):
    interact = ""
    tableau_k = ["" for i in range(len(valeur_one))]
    for i in range(len(valeur_one)):
        variable_one = valeur_one[i:i + 1]
        variable_two = valeur_two[i:i + 1]
        tableau_k[i] = "1" if variable_one == "1" or variable_two == "1" else "0"
    for i in tableau_k:
        interact += i
    return interact

def ETlogique(va11, valeur_two):
    interact = ""
    tableau_k = [""] * len(va11)
    for i in range(len(va11)):
        variable_one = va11[i:i + 1]
        variable_two = valeur_two[i:i + 1]
        tableau_k[i] = "1" if variable_one == "1" and variable_two == "1" else "0"
    interact = "".join(tableau_k)
    return interact

def permut(val, k):
    interact = ""
    tableau_k = [0] * len(val)
    for i in range(len(val)):
        id = k[i:i + 1]
        vid = int(id)
        tableau_k[i] = val[vid]
        interact += tableau_k[i]
    #print("interact permut", interact)
    return interact

#2

def inverse_permut(k):
    interact = ""
    tableau_k = [0] * len(k)
    for i in range(len(k)):
        id = k[i:i + 1]
        vid = int(id)
        tableau_k[vid] = str(i)
    interact = ''.join(tableau_k)
    #print("interact inverse", interact)
    return interact


def decalage(val, ordre, gauche):
    interact = ""
    tableau_k = [""] * len(val)
    s = -1 if gauche else 1
    for i in range(len(val)):
        variable_one = val[i:i + 1]
        o = ordre
        j = i
        while o > 0:
            if j + s < 0:
                j = len(val) - 1
            elif j + s >= len(val):
                j = 0
            else:
                j = j + s
            o -= 1
        tableau_k[j] = variable_one
    interact = "".join(tableau_k)
    return interact

def generateKey(k, pk, gdecalage, ddecalage):
    interact = ""
    nk = permut(k, pk)
    k1 = nk[0:4]
    k2 = nk[4:8]
    nk1 = OuExclusif(k1, k2)
    nk2 = ETlogique(k1, k2)
    dnk1 = decalage(nk1, gdecalage, True)
    dnk2 = decalage(nk2, ddecalage, False)
    interact = dnk1 + "," + dnk2
    #print("interact keygen " + interact)
    return interact

def roundDChiffre(val, kp, k):
    interact = ""
    perm = permut(val, kp)
    interact = OuExclusif(perm, k)
    return interact

#3

def inverse_permut(k):
    interact = ""
    tableau_k = [0] * len(k)
    for i in range(len(k)):
        id = k[i:i + 1]
        vid = int(id)
        tableau_k[vid] = str(i)
    interact = ''.join(tableau_k)
    # print("interact inverse", interact)
    return interact
    
def decalage(val, ordre, gauche):
    interact = ""
    tableau_k = ["" for _ in range(len(val))]
    s = -1 if gauche else 1
    for i in range(len(val)):
        variable_one = val[i:i + 1]
        o = ordre
        j = i
        while o > 0:
            if j + s < 0:
                j = len(val) - 1
            elif j + s >= len(val):
                j = 0
            else:
                j = j + s
            o -= 1
        tableau_k[j] = variable_one
    interact = "".join(tableau_k)
    return interact
    
def generateKey(k, pk, gdecalage, ddecalage):
    interact = ""
    nk = permut(k, pk)
    k1 = nk[0:4]
    k2 = nk[4:8]
    nk1 = OuExclusif(k1, k2)
    nk2 = ETlogique(k1, k2)
    dnk1 = decalage(nk1, gdecalage, True)
    dnk2 = decalage(nk2, ddecalage, False)
    interact = dnk1 + "," + dnk2
    # print("interact keygen " + interact)
    return interact
    
def roundDChiffre(val, kp, k):
    interact = ""
    perm = permut(val, kp)
    interact = OuExclusif(perm, k)
    return interact
    
def roundGChiffre(vald, valg, k):
    interact = ""
    fc = OuLogique(valg, k)
    interact = OuExclusif(vald, fc)
    return interact
    
def roundGDechiffre(val, kp, k):
    interact = ""
    nkp = inverse_permut(kp)
    c = OuExclusif(val, k)
    interact = permut(c, nkp)
    return interact
    
def roundDDechiffre(vald, valg, k):
    interact = ""
    fc = OuLogique(valg, k)
    interact = OuExclusif(vald, fc)
    return interact
    
def main():
    print("********ALGORITHME DE FREISNEL CIPHER*********")
    print("Donnez une clé K de longueur 8")
    key = input()
    while len(key) < 8:
        print("La taille de la clé doit être de longueur 8")
        key = input()
    print("Donnez la fonction H de permutation")
    h = input()
    while len(h) < 8:
        print("La taille doit être de longueur 8")
        h = input()
    decg = 0
    decd = 0
    print("Entrez l'ordre de décalage à gauche")
    decg = int(input())
    while decg <= 0:
        print("L'ordre doit être supérieur à 0")
        decg = int(input())
    print("Entrez l'ordre de décalage à droite")

#4

choix = int(input())
print("Entrez la permutation P de 4 bits")
p = input()
while len(p) < 4:
    print("La taille doit être de longueur 4")
    p = input()
print("Entrez la clé de permutation pour l'opération de chiffrement ou dechiffrement")
keyc = input()
while len(keyc) < 8:
    print("La taille doit être de longueur 8")
    keyc = input()
tkey = kgen.split(",")
if choix == 2:
    pn = permut(n, keyc)
    g0 = pn[:4]
    d0 = pn[4:8]
    d1 = roundDChiffre(g0, p, tkey[0])
    g1 = roundGChiffre(d0, g0, tkey[0])
    d2 = roundDChiffre(g1, p, tkey[1])
    g2 = roundGChiffre(d1, g1, tkey[1])
    c = g2 + d2
    ikey = inverse_permut(keyc)
    interact = permut(c, ikey)
    print("La valeur chiffrée est :", interact)
else:
    pn = permut(n, keyc)
    g2 = pn[:4]
    d2 = pn[4:8]
    g1 = roundGDechiffre(d2, p, tkey[1])
    d1 = roundDDechiffre(g2, g1, tkey[1])
    g0 = roundGDechiffre(d1, p, tkey[0])
    d0 = roundDDechiffre(g1, g0, tkey[0])
    Nd = g0 + d0
    ikey = inverse_permut(keyc)
    interact = permut(Nd, ikey)
    print("La valeur déchiffrée est :", interact)
main()

#Fin.