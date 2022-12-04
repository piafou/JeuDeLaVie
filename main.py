import pygame

#initialisation de pygame
pygame.init()

#Taille du tableau de la vie
largeur=72
hauteur=72
#Taille de la taille d'une brique elementaire d'une cellule (carré)
taillePixel=10
#epaisseur du quadrillage
tailleQuadrillage=1
#initialisation de notre tableau de vie
tableauDeVie=[[0 for x in range(largeur)] for y in range(hauteur)]
#initialisation des différentes couleurs du jeu
quadrillageCouleur=pygame.Color(50,50,200)
fondCouleur=pygame.Color(0,0,0)
celluleCouleur=pygame.Color(190,170,170)
#création de notre fenetre de jeux
ecran = pygame.display.set_mode((taillePixel*largeur+largeur*tailleQuadrillage+tailleQuadrillage, taillePixel*hauteur+hauteur*tailleQuadrillage+tailleQuadrillage))
ecran.fill(fondCouleur)
pygame.display.flip()
#titre de notre fenetre de jeux
pygame.display.set_caption("Le jeux de la vie !")
continuer = True
nDelai=50


#fonction qui dessine le quadrillage
def drawQuadrillage(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,quadrillageCouleur):
    #les pourtours
    pygame.draw.rect(ecran, quadrillageCouleur, pygame.Rect(0, 0, tailleQuadrillage+taillePixel, taillePixel*hauteur+hauteur*tailleQuadrillage+tailleQuadrillage))
    pygame.draw.rect(ecran, quadrillageCouleur, pygame.Rect(0, 0, taillePixel*largeur+largeur*tailleQuadrillage+tailleQuadrillage, taillePixel+tailleQuadrillage))
    pygame.draw.rect(ecran, quadrillageCouleur, pygame.Rect(taillePixel*(largeur-1)+(largeur-1)*tailleQuadrillage+tailleQuadrillage, 0, tailleQuadrillage+taillePixel, taillePixel*hauteur+hauteur*tailleQuadrillage+tailleQuadrillage))
    pygame.draw.rect(ecran, quadrillageCouleur, pygame.Rect(0, taillePixel*(hauteur-1)+(hauteur-1)*tailleQuadrillage+tailleQuadrillage, taillePixel*largeur+largeur*tailleQuadrillage+tailleQuadrillage, taillePixel+tailleQuadrillage))
    # les droites horizontales
    for x in range(largeur+1):
        pygame.draw.rect(ecran, quadrillageCouleur, pygame.Rect(x*(taillePixel+tailleQuadrillage), 0, tailleQuadrillage, taillePixel*hauteur+hauteur*tailleQuadrillage))
    # les droites verticales
    for y in range(hauteur+1):
        pygame.draw.rect(ecran, quadrillageCouleur, pygame.Rect(0, y*(taillePixel+tailleQuadrillage), taillePixel*largeur+largeur*tailleQuadrillage+tailleQuadrillage, tailleQuadrillage))

# on créé une brique de cellule
def Donnelavie(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,celluleCouleur,fondCouleur,pos,tableauDeVie,vie):
    x=pos[0]
    y=pos[1]
    xtableauDeVie=-1
    ytableauDeVie=-1
    for xTrav in range(1,largeur-1):
        if x < xTrav*tailleQuadrillage+taillePixel*(xTrav+1)  and x > xTrav*tailleQuadrillage+taillePixel*xTrav :
            xtableauDeVie=xTrav
    for yTrav in range(1,hauteur-1):
        if y < yTrav*tailleQuadrillage+taillePixel*(yTrav+1)  and y > yTrav*tailleQuadrillage+taillePixel*yTrav :
            ytableauDeVie=yTrav
    if xtableauDeVie !=-1 and ytableauDeVie !=-1 :
        if tableauDeVie[xtableauDeVie][ytableauDeVie]!=vie:
            tableauDeVie[xtableauDeVie][ytableauDeVie]=vie
        if vie==0:
            dessineUneBrique(ecran,taillePixel,tailleQuadrillage,fondCouleur,xtableauDeVie,ytableauDeVie)
        else:
            dessineUneBrique(ecran,taillePixel,tailleQuadrillage,celluleCouleur,xtableauDeVie,ytableauDeVie)

    pygame.display.flip()

# dessine une case du tableau
def dessineUneBrique(ecran,taillePixel,tailleQuadrillage,celluleCouleur,x,y):
     pygame.draw.rect(ecran, celluleCouleur, pygame.Rect(tailleQuadrillage+tailleQuadrillage*x+x*taillePixel,tailleQuadrillage+tailleQuadrillage*y+y*taillePixel, taillePixel, taillePixel))

#donne le nombre de cellules voisines vivantes
def voisin(tableauDeVie,largeur,hauteur,x,y):
    nVoisin = 0
    if x>0 and y>0 and x<largeur-1 and y<hauteur-1 :
        nVoisin=tableauDeVie[x-1][y-1] + tableauDeVie[x][y-1] + tableauDeVie[x+1][y-1] + tableauDeVie[x-1][y] + tableauDeVie[x+1][y] +tableauDeVie[x-1][y+1] + tableauDeVie[x][y+1] + tableauDeVie[x+1][y+1]
    return nVoisin

#Applique l'algo du jeu de la vie avance la vie d'un temps
def evolue(tableauDeVie,largeur,hauteur):
    tableauSuivant=[[0 for x in range(largeur)] for y in range(hauteur)]
    for x in range(largeur):
        for y in range(hauteur):
            tableauSuivant[x][y]=tableauDeVie[x][y]
    for x in range(largeur):
        for y in range(hauteur):
            nVoisin=voisin(tableauDeVie,largeur,hauteur,x,y)
            if tableauDeVie[x][y]==1:
                if nVoisin < 2 or nVoisin > 3:
                    tableauSuivant[x][y]=0
            else:
                if nVoisin==3:
                    tableauSuivant[x][y]=1
    for x in range(largeur):
        for y in range(hauteur):
            tableauDeVie[x][y]=tableauSuivant[x][y]
            
# dessine tous le tableau
def dessineTableau(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,celluleCouleur,fondCouleur,tableauDeVie):
    for x in range(1,largeur-1):
        for y in range(1,hauteur-1):
            if tableauDeVie[x][y] == 1:
                dessineUneBrique(ecran,taillePixel,tailleQuadrillage,celluleCouleur,x,y)
            else:
                dessineUneBrique(ecran,taillePixel,tailleQuadrillage,fondCouleur,x,y)
    pygame.display.flip()

 # fait un tableau vide et le redessine
def initialiser(ecran,tableauDeVie,largeur,hauteur,fondCouleur):
    for x in range(1,largeur-1):
        for y in range(1,hauteur-1):
            tableauDeVie[x][y]=0
            dessineUneBrique(ecran,taillePixel,tailleQuadrillage,fondCouleur,x,y)
    pygame.display.flip()




#Main c'est parti

drawQuadrillage(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,quadrillageCouleur)
pygame.display.flip()
bougeSouris = False
tempsPasse = False
vie=1
while continuer:
    if tempsPasse:
        evolue(tableauDeVie,largeur,hauteur)
        dessineTableau(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,celluleCouleur,fondCouleur,tableauDeVie)
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
                evolue(tableauDeVie,largeur,hauteur)
                dessineTableau(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,celluleCouleur,fondCouleur,tableauDeVie)
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not tempsPasse:
                bougeSouris = True
                vie=1
                Donnelavie(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,celluleCouleur,fondCouleur,event.pos,tableauDeVie,vie)
            if event.button == 2 and not tempsPasse:
                initialiser(ecran,tableauDeVie,largeur,hauteur,fondCouleur)               
            if event.button == 3 and not tempsPasse:
                bougeSouris = True
                vie=0
                Donnelavie(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,celluleCouleur,fondCouleur,event.pos,tableauDeVie,vie)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 or  event.button == 3:
                bougeSouris = False
        if event.type == pygame.MOUSEMOTION and bougeSouris:
            print(event.pos)
            Donnelavie(ecran,largeur,hauteur,taillePixel,tailleQuadrillage,celluleCouleur,fondCouleur,event.pos,tableauDeVie,vie)
    if tempsPasse:
        pygame.time.wait(nDelai)       

pygame.quit()
