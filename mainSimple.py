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
fondCouleur=pygame.Color(0,0,0)
celluleCouleur=pygame.Color(190,170,0)
#création de notre fenetre de jeux
ecran = pygame.display.set_mode((tailleCell*taille, tailleCell*taille))
ecran.fill(fondCouleur)
pygame.display.flip()
#titre de notre fenetre de jeux
pygame.display.set_caption("Le jeux de la vie !")
continuer = True
nDelai=50

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
def voisin(tableauDeVie,taille,x,y,cyclique):
    nVoisin = 0
    if cyclique:
        nVoisin=tableauDeVie[(x-1)%taille][(y-1)%taille] + tableauDeVie[x][(y-1)%taille] + tableauDeVie[(x+1)%taille][(y-1)%taille] + tableauDeVie[(x-1)%taille][y] + tableauDeVie[(x+1)%taille][y] +tableauDeVie[(x-1)%taille][(y+1)%taille] + tableauDeVie[x][(y+1)%taille] + tableauDeVie[(x+1)%taille][(y+1)%taille]
    else:
        if x>0 and y>0 and x<taille-1 and y<taille-1 :
            nVoisin=tableauDeVie[x-1][y-1] + tableauDeVie[x][y-1] + tableauDeVie[x+1][y-1] + tableauDeVie[x-1][y] + tableauDeVie[x+1][y] +tableauDeVie[x-1][y+1] + tableauDeVie[x][y+1] + tableauDeVie[x+1][y+1]
    return nVoisin

#Applique l'algo du jeu de la vie avance la vie d'un temps
def evolue(tableauDeVie,taille,cyclique):
    tableauSuivant=[[0 for x in range(taille)] for y in range(taille)]
    for x in range(taille):
        for y in range(taille):
            tableauSuivant[x][y]=tableauDeVie[x][y]
    for x in range(taille):
        for y in range(taille):
            nVoisin=voisin(tableauDeVie,taille,x,y,cyclique)
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
cyclique=True
while continuer:
    if tempsPasse:
        evolue(tableauDeVie,taille,cyclique)
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
                evolue(tableauDeVie,taille,cyclique)
                dessineTableau(ecran,taille,tailleCell,celluleCouleur,fondCouleur,tableauDeVie)
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
