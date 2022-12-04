import pygame

#initialisation de pygame
pygame.init()

#Taille du tableau de la vie
taille=100
#Taille de la taille d'une brique elementaire d'une cellule (carré)
tailleCell=10
#initialisation de notre tableau de vie
tableauDeVie=[[0 for x in range(taille)] for y in range(taille)]
#initialisation des différentes couleurs du jeu
quadrillageCouleur=pygame.Color(50,50,200)
fondCouleur=pygame.Color(50,50,0)
celluleCouleur=pygame.Color(190,170,0)
#création de notre fenetre de jeux
ecran = pygame.display.set_mode((tailleCell*taille, tailleCell*taille))
ecran.fill(fondCouleur)
pygame.display.flip()
#titre de notre fenetre de jeux
pygame.display.set_caption("Le jeux de la vie !")
continuer = True
nDelai=50


def planeur1(tableauDeVie,taille,celluleCouleur,x,y):
    xx=t(x//tailleCell,taille)
    yy=t(y//tailleCell,taille)
    dessineCell(ecran,tailleCell,celluleCouleur,xx,yy)
    tableauDeVie[xx][yy]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+1,taille),t(yy+1,taille))
    tableauDeVie[t(xx+1,taille)][t(yy+1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+2,taille),t(yy+1,taille))
    tableauDeVie[t(xx+2,taille)][t(yy+1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+2,taille),t(yy,taille))
    tableauDeVie[t(xx+2,taille)][t(yy,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+2,taille),t(yy-1,taille))
    tableauDeVie[t(xx+2,taille)][t(yy-1,taille)]=1
    pygame.display.flip()

def planeur2(tableauDeVie,taille,celluleCouleur,x,y):
    xx=t(x//tailleCell,taille)
    yy=t(y//tailleCell,taille)
    dessineCell(ecran,tailleCell,celluleCouleur,xx,yy)
    tableauDeVie[xx][yy]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx,taille),t(yy+2,taille))
    tableauDeVie[t(xx,taille)][t(yy+2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+1,taille),t(yy+3,taille))
    tableauDeVie[t(xx+1,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+2,taille),t(yy+3,taille))
    tableauDeVie[t(xx+2,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+3,taille),t(yy+3,taille))
    tableauDeVie[t(xx+3,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+4,taille),t(yy+3,taille))
    tableauDeVie[t(xx+4,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+4,taille),t(yy+2,taille))
    tableauDeVie[t(xx+4,taille)][t(yy+2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+4,taille),t(yy+1,taille))
    tableauDeVie[t(xx+4,taille)][t(yy+1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+3,taille),t(yy,taille))
    tableauDeVie[t(xx+3,taille)][t(yy,taille)]=1
    pygame.display.flip()

def canon(tableauDeVie,taille,celluleCouleur,x,y):
    xx=t(x//tailleCell,taille)
    yy=t(y//tailleCell,taille)
    dessineCell(ecran,tailleCell,celluleCouleur,xx,yy)
    tableauDeVie[xx][yy]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+1,taille),t(yy,taille))
    tableauDeVie[t(xx+1,taille)][t(yy,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx,taille),t(yy+1,taille))
    tableauDeVie[t(xx,taille)][t(yy+1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+1,taille),t(yy+1,taille))
    tableauDeVie[t(xx+1,taille)][t(yy+1,taille)]=1

    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+10,taille),t(yy,taille))
    tableauDeVie[t(xx+10,taille)][t(yy,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+10,taille),t(yy-1,taille))
    tableauDeVie[t(xx+10,taille)][t(yy-1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+10,taille),t(yy+1,taille))
    tableauDeVie[t(xx+10,taille)][t(yy+1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+11,taille),t(yy+2,taille))
    tableauDeVie[t(xx+11,taille)][t(yy+2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+12,taille),t(yy+3,taille))
    tableauDeVie[t(xx+12,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+13,taille),t(yy+3,taille))
    tableauDeVie[t(xx+13,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+11,taille),t(yy-2,taille))
    tableauDeVie[t(xx+11,taille)][t(yy-2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+12,taille),t(yy-3,taille))
    tableauDeVie[t(xx+12,taille)][t(yy-3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+13,taille),t(yy-3,taille))
    tableauDeVie[t(xx+13,taille)][t(yy-3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+14,taille),t(yy,taille))
    tableauDeVie[t(xx+14,taille)][t(yy,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+15,taille),t(yy-2,taille))
    tableauDeVie[t(xx+15,taille)][t(yy-2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+15,taille),t(yy+2,taille))
    tableauDeVie[t(xx+15,taille)][t(yy+2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+16,taille),t(yy-1,taille))
    tableauDeVie[t(xx+16,taille)][t(yy-1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+16,taille),t(yy+1,taille))
    tableauDeVie[t(xx+16,taille)][t(yy+1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+16,taille),t(yy,taille))
    tableauDeVie[t(xx+16,taille)][t(yy,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+17,taille),t(yy,taille))
    tableauDeVie[t(xx+17,taille)][t(yy,taille)]=1

    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+20,taille),t(yy+1,taille))
    tableauDeVie[t(xx+20,taille)][t(yy+1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+20,taille),t(yy+2,taille))
    tableauDeVie[t(xx+20,taille)][t(yy+2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+20,taille),t(yy+3,taille))
    tableauDeVie[t(xx+20,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+21,taille),t(yy+1,taille))
    tableauDeVie[t(xx+21,taille)][t(yy+1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+21,taille),t(yy+2,taille))
    tableauDeVie[t(xx+21,taille)][t(yy+2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+21,taille),t(yy+3,taille))
    tableauDeVie[t(xx+21,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+22,taille),t(yy+4,taille))
    tableauDeVie[t(xx+22,taille)][t(yy+4,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+22,taille),t(yy,taille))
    tableauDeVie[t(xx+22,taille)][t(yy,taille)]=1

    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+24,taille),t(yy,taille))
    tableauDeVie[t(xx+24,taille)][t(yy,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+24,taille),t(yy-1,taille))
    tableauDeVie[t(xx+24,taille)][t(yy-1,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+24,taille),t(yy+4,taille))
    tableauDeVie[t(xx+24,taille)][t(yy+4,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+24,taille),t(yy+5,taille))
    tableauDeVie[t(xx+24,taille)][t(yy+5,taille)]=1

    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+34,taille),t(yy+2,taille))
    tableauDeVie[t(xx+34,taille)][t(yy+2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+34,taille),t(yy+3,taille))
    tableauDeVie[t(xx+34,taille)][t(yy+3,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+35,taille),t(yy+2,taille))
    tableauDeVie[t(xx+35,taille)][t(yy+2,taille)]=1
    dessineCell(ecran,tailleCell,celluleCouleur,t(xx+35,taille),t(yy+3,taille))
    tableauDeVie[t(xx+35,taille)][t(yy+3,taille)]=1
    pygame.display.flip()     

def t(value,taille):
    return value%taille


# on modifie le tableau par l'interface
def Modifie(ecran,taille,tailleCell,celluleCouleur,fondCouleur,pos,tableauDeVie,vie):
    x=pos[0]
    y=pos[1]
    if vie == 1:
        couleur=celluleCouleur
    else:
        couleur=fondCouleur
    dessineCell(ecran,tailleCell,couleur,x//tailleCell,y//tailleCell)
    tableauDeVie[x//tailleCell][y//tailleCell]=vie
    pygame.display.flip()

# dessine une case du tableau
def dessineCell(ecran,tailleCell,couleur,x,y):
     pygame.draw.rect(ecran, couleur, pygame.Rect(x*tailleCell,y*tailleCell, tailleCell, tailleCell))

#donne le nombre de cellules voisines vivantes
def voisin(tableauDeVie,taille,x,y):
    return tableauDeVie[(x-1)%taille][(y-1)%taille] + tableauDeVie[x][(y-1)%taille] + tableauDeVie[(x+1)%taille][(y-1)%taille] + tableauDeVie[(x-1)%taille][y] + tableauDeVie[(x+1)%taille][y] +tableauDeVie[(x-1)%taille][(y+1)%taille] + tableauDeVie[x][(y+1)%taille] + tableauDeVie[(x+1)%taille][(y+1)%taille]

#Applique l'algo du jeu de la vie avance la vie d'un temps
def evolue(tableauDeVie,taille):
    tableauSuivant=[[0 for x in range(taille)] for y in range(taille)]
    for x in range(taille):
        for y in range(taille):
            tableauSuivant[x][y]=tableauDeVie[x][y]
    for x in range(taille):
        for y in range(taille):
            nVoisin=voisin(tableauDeVie,taille,x,y)
            if tableauDeVie[x][y]==1:
                if nVoisin < 2 or nVoisin > 3:
                    tableauSuivant[x][y]=0
            else:
                if nVoisin==3:
                    tableauSuivant[x][y]=1
    for x in range(taille):
        for y in range(taille):
            tableauDeVie[x][y]=tableauSuivant[x][y]
            
# dessine tous le tableau
def dessineTableau(ecran,taille,tailleCell,celluleCouleur,fondCouleur,tableauDeVie):
    for x in range(taille):
        for y in range(taille):
            if tableauDeVie[x][y] == 1:
                dessineCell(ecran,tailleCell,celluleCouleur,x,y)
            else:
                dessineCell(ecran,tailleCell,fondCouleur,x,y)
    pygame.display.flip()

 # fait un tableau vide et le redessine
def initialiser(ecran,tableauDeVie,taille,fondCouleur):
    for x in range(taille):
        for y in range(taille):
            tableauDeVie[x][y]=0
    ecran.fill(fondCouleur)
    pygame.display.flip()




#Main c'est parti
pygame.display.flip()
bougeSouris = False
tempsPasse = False
vie=1
while continuer:
    if tempsPasse:
        evolue(tableauDeVie,taille)
        dessineTableau(ecran,taille,tailleCell,celluleCouleur,fondCouleur,tableauDeVie)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                tempsPasse= not tempsPasse
                if tempsPasse:
                    pygame.display.set_caption("Le jeux de la vie ! le temps passe")
                    bougeSouris = False
                else:
                    pygame.display.set_caption("Le jeux de la vie ! le temps est arrété")
            elif event.key==pygame.K_ESCAPE:
                continuer = False
            elif event.key==pygame.K_RIGHT:
                tempsPasse = False
                evolue(tableauDeVie,taille)
                dessineTableau(ecran,taille,tailleCell,celluleCouleur,fondCouleur,tableauDeVie)
            elif event.key==pygame.K_1:
                if not tempsPasse:
                    pos=pygame.mouse.get_pos()
                    planeur1(tableauDeVie,taille,celluleCouleur,pos[0],pos[1])
            elif event.key==pygame.K_2:
                if not tempsPasse:
                    pos=pygame.mouse.get_pos()
                    planeur2(tableauDeVie,taille,celluleCouleur,pos[0],pos[1])
            elif event.key==pygame.K_3:
                if not tempsPasse:
                    pos=pygame.mouse.get_pos()
                    canon(tableauDeVie,taille,celluleCouleur,pos[0],pos[1])
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not tempsPasse:
                bougeSouris = True
                vie=1
                Modifie(ecran,taille,tailleCell,celluleCouleur,fondCouleur,event.pos,tableauDeVie,vie)
            if event.button == 2 and not tempsPasse:
                initialiser(ecran,tableauDeVie,taille,fondCouleur)               
            if event.button == 3 and not tempsPasse:
                bougeSouris = True
                vie=0
                Modifie(ecran,taille,tailleCell,celluleCouleur,fondCouleur,event.pos,tableauDeVie,vie)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 or  event.button == 3:
                bougeSouris = False
        if event.type == pygame.MOUSEMOTION and bougeSouris:
            Modifie(ecran,taille,tailleCell,celluleCouleur,fondCouleur,event.pos,tableauDeVie,vie)
    if tempsPasse:
        pygame.time.wait(nDelai)       

pygame.quit()
