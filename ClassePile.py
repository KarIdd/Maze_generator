from random import *

class Pile:
    '''création d'une instance Pile avec une liste que l'on nommera L'''
    def __init__(self):
        '''Initialisation des 2 attributs : une liste L vide et la taille de la pile'''
        self.L=[]
        self.taille=0

    def vide(self):
        """test si la pile est vide en retournant Vrai si c’est le cas"""
        return self.taille==0

    def depiler(self):
        """retourne la pile à laquelle on a enlevé le sommet """
        assert(self.taille != 0),"la pile est déjà vide"
        self.taille-=1
        return self.L.pop()

    def empiler(self,x):
        """retourne la pile avec pour sommet x"""
        self.L.append(x)
        self.taille+=1
        
    def longueur(self):
        """retourne la taille de la pile"""
        return self.taille
    
    def sommet(self):
        """retourne le sommet de la pile"""
        assert(self.taille != 0),"""la pile est vide, elle n''a pas de sommet"""
        return self.L[self.taille-1]
    
    def melanger(self):
        return shuffle(self.L)