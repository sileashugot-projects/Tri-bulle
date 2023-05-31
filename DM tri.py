'''
Noms: Alexandre, Max, Siléas
Classe : 1e spe NSI
DM: tri à bulle
Date: 2/22/2022
'''
import random
# Exercice 1
def bulle(T):
    '''
    Fonction avec une liste comme parametre et renvoi une liste triée (le tri à bulle)
    '''
    trie=1
    comparaisons=0       # Compteur de comparaisons
    echanges=0           # Compteur d'echanges
    while trie==1:   # La condition est tant qu'on fait au moins un echange dans la boucle
        trie=0       # Si la variable reste à 0 apres la boucle, la liste est triee est on peut sortir de la boucle tant que
        for i in range(len(T)-1):
            comparaisons+=1
            if T[i]>T[i+1]:
                echanges+=1
                trie=1
                T[i],T[i+1]=T[i+1],T[i]
    return T,echanges,comparaisons

def shaker(T):
    '''
    Fonction avec une liste comme parametre et renvoi une liste triée (le tri shaker)
    '''
    trie=1
    start,fin=0,len(T)-1
    echange=0
    while trie==1:
        trie=0
        for i in range(start,fin):
            if T[i]>T[i+1]:
                echange+=1
                trie=1
                T[i],T[i+1]=T[i+1],T[i]
        start+=1
        T=list(reversed(T))
        for i in range(start,fin):
            if T[i]<T[i+1]:
                echange+=1
                trie=1
                T[i],T[i+1]=T[i+1],T[i]
        fin-=1
        T=list(reversed(T))
    return T,echange

n=int(input())
a=[random.randint(0,n) for i in range (n)]
