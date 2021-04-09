# import des librairies et des fonctions
import ClassePile as cp
import matplotlib.pyplot as plt

class Labyrinthe:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.cells=[]
        self.ouvert=0
        number=0

        # créé des cellules numérotées
        for a in range (self.height):
            self.cells.append([])
            for b in range (self.width):
                number+=1
                self.cells[a].append({'N':False,'E':False,'S':False,'O':False,'zone':number}) # direction=False <=> mur
    
    def print_plot(self):
        # trace le labyrinthe avec la librairie matplotlib
        for a in range (self.height):
            for b in range (self.width):
                if self.cells[a][b]['N']==False:
                    plt.plot([b,b+1],[self.height-a,self.height-a],'b')
                if self.cells[a][b]['S']==False:
                    plt.plot([b,b+1],[self.height-(a+1),self.height-(a+1)],'b')
                if self.cells[a][b]['O']==False:
                    plt.plot([b,b],[self.height-a,self.height-(a+1)],'b')
                if self.cells[a][b]['E']==False:
                    plt.plot([b+1,b+1],[self.height-a,self.height-(a+1)],'b')
        plt.show()

    def peindre(self, i, j, origine, valeur):
        # change les valeurs des cellules
        if i<0 or i>=self.height or j<0 or j>=self.width:
            return None
        else:
            if self.cells[i][j]['zone']==valeur:
                self.cells[i][j]['zone']=origine
                self.peindre(i, j-1, origine, valeur)
                self.peindre(i, j+1, origine, valeur)
                self.peindre(i-1, j, origine, valeur)
                self.peindre(i+1, j, origine, valeur)


    def fusionner(self, i, j, dir):
        # peind les cellules adjacentes différentes à la valeur de la zone séléctionnée
        zone = self.cells[i][j]["zone"]
        if  dir == "E" and self.cells[i][j+1]["zone"] != zone:
            self.ouvert += 1
            self.cells[i][j]["E"] = True
            self.cells[i][j+1]["O"] = True
            self.peindre(i, j+1, zone, self.cells[i][j+1]["zone"])

        elif  dir == "O" and self.cells[i][j-1]["zone"] != zone:
            self.ouvert += 1
            self.cells[i][j]["O"] = True
            self.cells[i][j-1]["E"] = True
            self.peindre(i, j-1, zone, self.cells[i][j-1]["zone"])

        elif  dir == "N" and self.cells[i-1][j]["zone"] != zone:
            self.ouvert += 1
            self.cells[i][j]["N"] = True
            self.cells[i-1][j]["S"] = True
            self.peindre(i-1, j, zone, self.cells[i-1][j]["zone"])

        elif  dir == "S" and self.cells[i+1][j]["zone"] != zone:
            self.ouvert += 1
            self.cells[i][j]["S"] = True
            self.cells[i+1][j]["N"] = True
            self.peindre(i+1, j, zone, self.cells[i+1][j]["zone"])

        else:
            return False
        
    def generer(self):
        # ouvre les murs du labyrinthe pour créer des zones à peindre
        murs = cp.Pile()
        for i in range(self.height):
            for j in range(self.width):
                if i != 0:
                    murs.empiler((i, j, "N"))
                if i != self.height-1:
                    murs.empiler((i, j, "S"))
                if j != 0:
                    murs.empiler((i, j, "O"))
                if j != self.width-1:
                    murs.empiler((i, j, "E"))
        murs.melanger()
        while self.ouvert < (self.height * self.width-1):
            monMur = murs.depiler()
            self.fusionner(monMur[0], monMur[1], monMur[2])
        
        
        
    def afficher(self):
        return self.cells
            

#taille du labyrinthe
laby=Labyrinthe(20,20)

laby.generer()
laby.print_plot()
