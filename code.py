import pyxel

class App:

    def __init__(self):
        pyxel.init(240, 140, title="phantom castle", fps=40, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("images.pyxres") #charger l'image
        self.couleur_fond = 0 #couleur du fond, noir au début
        self.etat = "prison" #le stade du jeu
        self.temps = pyxel.frame_count #sert à stocker la valeur du temps, sera ensuite modifié pour faire des calculs
        self.coordonnee_perso = [0, 95] #coordonnées du personnage
        self.vitesse_perso = 5 #vitesse du personnage
        self.t_labyrinthe = [[(0,20),1,2,1,(0,16),1], [(0,20),1,2,1,(0,16),1], [2,(1,13),(0,5),1,2,1,2,(1,8),2,(1,5),2,(1,3),], [2, 1,(0,8),1,2,1,2,(1,4),2,1,2,(1,3),(0,16),1], [2,1,(0,8),1,2,1,2,1,(0,5),1,(0,4),1,(0,16),1], [2,1,2,(1,4),2,1,2,1,2,1,(0,5),1,(0,4),(1,3),2,(1,5),2,(1,6)], [2,1,2,1,2,1,2,1,2,1,2,1,2,(1,6),2,1,(0,8),1,2,1,2,1], [(0,5),1,2,1,2,1,2,1,(0,7),1,(0,5),1,(0,8),1,2,1,2,1,2,(1,2)], [(0,5),1,2,1,2,1,2,1,(0,7),1,(0,5),1,2,(1,4),2,1,2,1,2,1], [(1,3),2,1,(0,5),1,2,(1,6),2,1,2,(1,4),2,1,(0,5),1,2,1,2,1], [(0,5),1,(0,5),1,(0,7),1,2,1,(0,8),1,(0,5),(1,4),2,(1,3)], [(0,5),1,2,1,2,1,(0,7),1,2,1,(0,8),1,2,1,2,1,(0,7),1], [2,1,2,1,2,1,2,1,2,(1,6),2,1,2,(1,4),2,1,2,1,2,1,(0,7),1], [2,1,2,1,2,1,2,1,(0,4),1,(0,5),1,2,1,(0,5),1,2,(1,4),2,(1,3),2,1], [2,1,2,1,2,1,2,1,(0,4),1,(0,5),1,2,1,(0,5),1,(0,8),(1,3),2,1], [(1,3),2,1,2,1,2,(1,3),2,1,2,(1,4),2,1,2,(1,4),(0,8),(1,3),2,1], [(0,8),1,2,1,(0,4),1,2,1,(0,5),1,2,(1,15),2,1], [(0,8),1,2,1,(0,4),1,2,1,(0,5),1,(0,16),1,2,1], [2,(1,7),2,1,2,(1,3),2,(1,7),(0,16),1,2,1], [2,1,(0,8),1,(0,17),(1,14),2,1], [2,1,(0,8),1,(0,17),1,(0,15),1], [2,1,2,(1,9),2,(1,8),2,(1,4),(0,15),1], [2,1,(0,10),1,2,1,(0,9),1,2,1,2,(1,14)], [2,1,(0,10),1,2,1,(0,9),1,2,1,(0,15),1], [2,(1,6),2,1,2,1,2,1,2,(1,5),2,1,2,1,(0,15),1], [2,1,(0,7),1,2,1,2,1,2,(1,5),2,1,2,1,2,(1,8),2,1,2,1], [2,1,(0,7),1,(0,5),1,(0,12),1,2,1,(0,9),1], [2,1,(0,7),1,(0,5),1,(0,12),1,2,1,(0,9),1]]
        self.tab_labyrinthe = []
        for ligne in self.t_labyrinthe:
            tab = []
            for couple in ligne:
                if couple == 1:
                    tab.append(1)
                elif couple == 2:
                    tab.append(0)
                    tab.append(0)
                else:
                    for i in range(couple[1]):
                        tab.append(couple[0])
            self.tab_labyrinthe.append(tab)
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE): #la touche espace permet de modifier l'affichage de l'écran

            if self.etat == "titre" and pyxel.frame_count - self.temps > 10: #changer l'écran après le titre
                self.etat = "texte"
                pyxel.cls(0)
                self.temps = pyxel.frame_count

            elif self.etat == "texte" and pyxel.frame_count - self.temps > 10: #changer l'écran après le texte
                pyxel.cls(0)
                self.etat = "chateau"
                self.temps = pyxel.frame_count

            elif self.etat == "chateau" and pyxel.frame_count - self.temps > 10: #changer l'écran après le chateau
                pyxel.cls(0)
                self.etat = "entrer dans le chateau"
                self.temps = pyxel.frame_count
                self.souris(True)
            elif self.etat == "prison" and pyxel.frame_count - self.temps > 10: #changer l'écran après la grille
                pyxel.cls(6)
                self.etat = "couloir"
                self.temps = pyxel.frame_count

        if self.etat == "entrer dans le chateau" or self.etat == "couloir":
            if pyxel.btn(pyxel.KEY_LEFT) and self.coordonnee_perso[0] > 0: #le personnage va à gauche, mais ne peut pas sortir de la fenêtre d'affichage
                self.coordonnee_perso[0] = self.coordonnee_perso[0] - self.vitesse_perso

            if pyxel.btn(pyxel.KEY_RIGHT) and self.coordonnee_perso[0] < 235: #le personnage va à droite
                self.coordonnee_perso[0] = self.coordonnee_perso[0] + self.vitesse_perso

            if self.coordonnee_perso[0] >= 235: #si le personnage sort à droite, on change l'image
                self.temps = pyxel.frame_count
                if self.etat == "entrer dans le chateau":
                    self.etat = "grille"

        if self.etat == "prison":
            self.coordonnee_perso = [230, 118]
            pyxel.cls(0)

        if self.etat == "couloir":
            if pyxel.btn(pyxel.KEY_RETURN) and self.coordonnee_perso[0] > 95 and self.coordonnee_perso[0] < 120:
                self.etat = "labyrinthe"




    def draw(self):
        if self.etat == "titre": #afficher l'image avec le titre
            self.cadre()
            self.titre()
        elif self.etat == "texte": #afficher l'image avec le texte
            self.cadre()
            self.texte()
        elif self.etat == "chateau": #afficher l'image avec le chateau
            self.chateau()
        elif self.etat == "entrer dans le chateau": #afficher l'image ou on doit faire entrer le personnage dans le chateau
            pyxel.cls(1)
            self.entrer_chateau()
            pyxel.blt(self.coordonnee_perso[0], self.coordonnee_perso[1], 0, 0, 33, 9, 23, 8)
        elif self.etat == "grille": #affiche la grille, on voit le personnage entrer dans le chateau
            pyxel.cls(0)
            self.ouverture_grille(self.temps)
        elif self.etat == "couloir":
            self.couloir()
            pyxel.blt(self.coordonnee_perso[0], self.coordonnee_perso[1], 0, 0, 33, 9, 23, 8)
        elif self.etat == "labyrinthe":
            self.labyrinthe()



    def labyrinthe(self):
        pyxel.cls(13)
        for i_ligne in range(len(self.tab_labyrinthe)):

            for i_colonne in range(len(self.tab_labyrinthe[i_ligne])):
                if self.tab_labyrinthe[i_ligne][i_colonne] == 1:
                    pyxel.blt(i_colonne*5, i_ligne*5, 1, 40, 112, 5, 5, 0)


    def couloir(self):
        pyxel.bltm(0, 0, 0, 0, 0, 64, 128, 0)
        pyxel.bltm(64, 0, 0, 0, 0, 64, 128, 0)
        pyxel.bltm(128, 0, 0, 0, 0, 64, 128, 0)
        pyxel.bltm(192, 0, 0, 0, 0, 48, 128, 0)
        pyxel.bltm(0, 128, 0, 0, 0, 64, 12, 0)
        pyxel.bltm(64, 128, 0, 0, 0, 64, 12, 0)
        pyxel.bltm(128, 128, 0, 0, 0, 64, 12, 0)
        pyxel.bltm(192, 128, 0, 0, 0, 48, 12, 0)
        pyxel.blt(10, 79, 1, 0, 112, 32, 64, 0)#porte 1
        pyxel.blt(52, 79, 1, 0, 112, 32, 64, 0)#porte 2
        pyxel.blt(94, 79, 1, 0, 112, 32, 64, 0)#porte 3
        pyxel.blt(22, 94, 0, 18, 35, 2, 5, 0)#1
        pyxel.blt(26, 94, 0, 21, 35, 4, 5, 0)#8
        pyxel.blt(66, 94, 0, 26, 35, 4, 5, 0)#6
        pyxel.blt(108, 94, 0, 21, 35, 4, 5, 0)#8


    def ouverture_grille(self, temps):
        pyxel.bltm(0, 0, 0, 0, 0, 120, 140) #mur de brique (partie gauche)
        pyxel.bltm(119, 0, 0, 0, 0, -121, 140) #mur de brique (partie droite)

        pyxel.line(70, 140, 70, 70, 0) #ligne gauche de l'encadrement de porte
        pyxel.line(169, 140, 169, 70, 0) #ligne droite de l'encadrement de porte
        pyxel.elli(71, 35, 98, 75,  0) #l'arrondi au dessus de l'encadrement de porte

        x = 140 #change de valeur pour donner l'impression que la grille s'ouvre et se ferme
        endroit = "dehors" #permet d'afficher le personnage devant ou derière la grille
        if pyxel.frame_count < temps + 10:
            x = 140
        elif pyxel.frame_count < temps + 20:
            x = 130
        elif pyxel.frame_count < temps + 30:
            x = 120
        elif pyxel.frame_count < temps + 40:
            x = 110
        elif pyxel.frame_count < temps + 50:
            x = 100
        elif pyxel.frame_count < temps + 60:
            x = 90
        elif pyxel.frame_count < temps + 70:
            x = 80
        elif pyxel.frame_count < temps + 80:
            x = 90
            endroit = "dedans"
        elif pyxel.frame_count < temps + 90:
            x = 100
            endroit = "dedans"
        elif pyxel.frame_count < temps + 100:
            x = 110
            endroit = "dedans"
        elif pyxel.frame_count < temps + 110:
            x = 120
            endroit = "dedans"
        elif pyxel.frame_count < temps + 120:
            x = 130
            endroit = "dedans"
        elif pyxel.frame_count < temps + 130:
            x = 140
            endroit = "dedans"
        else:
            self.etat = "prison"
        if self.etat != "prison":
            if endroit == "dedans": #afficher le personnage derrière la grille
                pyxel.blt(116, 117, 0, 0, 33, 9, 23, 8)

            #dessiner tous les barreaux de la grille
            #1
            pyxel.line(73, x - 1, 73, 61, 7)
            pyxel.line(74, x, 74, 59, 7)
            pyxel.line(75, x - 1, 75, 57, 7)
            #2
            pyxel.line(80, x - 1, 80, 50, 7)
            pyxel.line(81, x, 81, 49, 7)
            pyxel.line(82, x - 1, 82, 49, 7)
            #3
            pyxel.line(87, x - 1, 87, 45, 7)
            pyxel.line(88, x, 88, 44, 7)
            pyxel.line(89, x - 1, 89, 43, 7)
            #4
            pyxel.line(94, x - 1, 94, 41, 7)
            pyxel.line(95, x, 95, 40, 7)
            pyxel.line(96, x - 1, 96, 40, 7)
            #5
            pyxel.line(101, x - 1, 101, 38, 7)
            pyxel.line(102, x, 102, 37, 7)
            pyxel.line(103, x - 1, 103, 37, 7)
            #6
            pyxel.line(108, x - 1, 108, 36, 7)
            pyxel.line(109, x, 109, 36, 7)
            pyxel.line(110, x - 1, 110, 36, 7)
            #7
            pyxel.line(115, x - 1, 115, 35, 7)
            pyxel.line(116, x, 116, 35, 7)
            pyxel.line(117, x - 1, 117, 35, 7)
            #8
            pyxel.line(122, x - 1, 122, 35, 7)
            pyxel.line(123, x, 123, 35, 7)
            pyxel.line(124, x - 1, 124, 35, 7)
            #9
            pyxel.line(129, x - 1, 129, 36, 7)
            pyxel.line(130, x, 130, 36, 7)
            pyxel.line(131, x - 1, 131, 36, 7)
            #10
            pyxel.line(136, x - 1, 136, 37, 7)
            pyxel.line(137, x, 137, 37, 7)
            pyxel.line(138, x - 1, 138, 38, 7)
            #11
            pyxel.line(143, x - 1, 143, 40, 7)
            pyxel.line(144, x, 144, 40, 7)
            pyxel.line(145, x - 1, 145, 41, 7)
            #12
            pyxel.line(150, x - 1, 150, 43, 7)
            pyxel.line(151, x, 151, 44, 7)
            pyxel.line(152, x - 1, 152, 45, 7)
            #13
            pyxel.line(157, x - 1, 157, 49, 7)
            pyxel.line(158, x, 158, 49, 7)
            pyxel.line(159, x - 1, 159, 50, 7)
            #14
            pyxel.line(164, x - 1, 164, 57, 7)
            pyxel.line(165, x, 165, 59, 7)
            pyxel.line(166, x - 1, 166, 61, 7)
            if endroit == "dehors": #permet d'afficher le personnage devant la grille
                pyxel.blt(116, 117, 0, 0, 33, 9, 23, 8)


    def entrer_chateau(self):
        """Cette fonction dessine l'image pour entrer dans le chateau"""
        pyxel.blt(0, 90, 2, 0, 0, 20, 21, 0) #le panneau
        pyxel.line(0, 110, 240, 110, 3) #la ligne d'herbe

        for y in range(111, 141): #le chemin
            pyxel.line(0, y, 240, y, 13)

        for x in [30, 70, 108, 156]: #les tronc d'arbres
            for y in range(65, 110):
                pyxel.line(x, y, x+9, y , 4)
            #les brins d'herbes + les feuilles des arbres
            pyxel.blt(x - 2, 108, 2, 24, 1, 3, 2, 0)
            pyxel.blt(x + 9, 108, 2, 28, 0, 2, 3, 0)
            pyxel.blt(x - 15, 50, 2, 0, 25, 38, 50, 0)
            #le bout du mur de brique
            for y in [90, 75, 60, 45, 30, 15, 0]:
                pyxel.blt(224, y, 1, 0, 41, 16, 15, 0)
            pyxel.blt(224, 105, 1, 0, 41, 16, 6, 0)


    def cadre(self):
        """La fonction dessine un cadre."""
        for x in range(pyxel.width): #fait les contours
            for y in range(pyxel.height):
                if x <= 2 or x >= pyxel.width-3 or y <= 2 or y >= pyxel.height-3:
                    pyxel.pset(x, y, 4)
        pyxel.blt(2, 122, 0, 0, 16, 16, 16, 0) #coin bas gauche
        pyxel.blt(2, 2, 0, 0, 16, 16, -16, 0) #coin haut gauche
        pyxel.blt(222, 122, 0, 0, 16, -16, 16, 0) #coin bas droit
        pyxel.blt(222, 2, 0, 0, 16, -16, -16, 0) #coin haut droit


    def titre(self):
        """La fonction écrit le titre du projet."""
        pyxel.blt(91, 57, 0, 16, 0, 6, 8, 0) #P
        pyxel.blt(98, 57, 0, 24, 0, 8, 8, 0) #H
        pyxel.blt(107, 57, 0, 32, 0, 8, 8, 0) #A
        pyxel.blt(116, 57, 0, 40, 0, 8, 8, 0) #N
        pyxel.blt(125, 57, 0, 48, 0, 7, 8, 0) #T
        pyxel.blt(133, 57, 0, 55, 0, 6, 8, 0) #O
        pyxel.blt(140, 57, 0, 16, 8, 9, 8, 0) #M

        pyxel.blt(98, 67, 0, 25, 8, 6, 8, 0) #C
        pyxel.blt(105, 67, 0, 32, 0, 8, 8, 0) #A
        pyxel.blt(114, 67, 0, 32, 8, 6, 8, 0) #S
        pyxel.blt(121, 67, 0, 48, 0, 7, 8, 0) #T
        pyxel.blt(129, 67, 0, 38, 8, 6, 8, 0) #L
        pyxel.blt(136, 67, 0, 44, 8, 6, 8, 0) #E

    def chateau(self):
        """La fonction dessine le chateau."""
        pyxel.blt(50, 70, 1, 0, 0, 25, 70, 0) #tour gauche
        pyxel.blt(164, 70, 1, 0, 0, 25, 70, 0) #tour droite
        pyxel.blt(75, 40, 1, 32, 0, 90, 101, 0)

    def texte(self):
        """La fonction écrit le texte d'intro."""
        pyxel.blt(44, 40, 0, 50, 8, 3, 8, 0)#I
        pyxel.blt(48, 40, 0, 16, 16, 2, 8, 0)#l

        pyxel.blt(54, 39, 0, 16, 24, 5, 11, 0)#é
        pyxel.blt(60, 40, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(66, 42, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(72, 40, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(74, 40, 0, 21, 24, 5, 8, 0)#t

        pyxel.blt(82, 42, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(88, 42, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(94, 42, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(102, 40, 0, 32, 24, 3, 8, 0)#f
        pyxel.blt(106, 42, 0, 35, 26, 5, 6, 0)#o
        pyxel.blt(112, 40, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(114, 42, 0, 40, 26, 5, 6, 0)#s

        pyxel.blt(120, 46, 0, 39, 21, 2, 3, 0)#,

        pyxel.blt(124, 42, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(130, 42, 0, 27, 18, 5, 6, 0)#u

        pyxel.blt(138, 40, 0, 41, 16, 4, 8, 0)#j
        pyxel.blt(143, 42, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(149, 42, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(155, 42, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(161, 42, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(169, 40, 0, 46, 16, 6, 8, 0)#h
        pyxel.blt(175, 42, 0, 35, 26, 5, 6, 0)#o
        pyxel.blt(181, 42, 0, 46, 26, 6, 6, 0)#m
        pyxel.blt(187, 42, 0, 46, 26, 6, 6, 0)#m
        pyxel.blt(193, 42, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(44, 53, 0, 54, 10, 5, 9, 0)#p
        pyxel.blt(50, 53, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(56, 53, 0, 60, 10, 5, 6, 0)#r
        pyxel.blt(62, 51, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(68, 53, 0, 21, 18, 5, 6, 0)#u

        pyxel.blt(77, 51, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(83, 53, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(89, 53, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(95, 53, 0, 40, 26, 5, 6, 0)#s

        pyxel.blt(103, 51, 0, 16, 16, 2, 8, 0)#l
        pyxel.blt(106, 53, 0, 26, 26, 5, 6, 0)#a

        pyxel.blt(114, 51, 0, 32, 24, 3, 8, 0)#f
        pyxel.blt(118, 53, 0, 35, 26, 5, 6, 0)#o
        pyxel.blt(124, 53, 0, 60, 10, 5, 6, 0)#r
        pyxel.blt(130, 50, 0, 66, 8, 5, 9, 0)#ê
        pyxel.blt(136, 51, 0, 21, 24, 5, 8, 0)#t

        pyxel.blt(144, 53, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(150, 53, 0, 35, 26, 5, 6, 0)#o
        pyxel.blt(156, 51, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(158, 53, 0, 60, 10, 5, 6, 0)#r
        pyxel.blt(164, 53, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(170, 58, 0, 69, 20, 1, 1, 0)#.

        pyxel.blt(174, 51, 0, 32, 0, 8, 8, 0)#A

        pyxel.blt(185, 51, 0, 16, 16, 2, 8, 0)#l
        pyxel.blt(188, 53, 0, 26, 26, 5, 6, 0)#a

        pyxel.blt(44, 64, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(50, 64, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(56, 62, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(58, 62, 0, 21, 24, 5, 8, 0)#t

        pyxel.blt(66, 62, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(72, 64, 0, 35, 26, 5, 6, 0)#o
        pyxel.blt(78, 64, 0, 46, 26, 6, 6, 0)#m
        pyxel.blt(85, 62, 0, 72, 17, 5, 8, 0)#b
        pyxel.blt(91, 61, 0, 16, 24, 5, 9, 0)#é
        pyxel.blt(97, 64, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(103, 68, 0, 65, 18, 2, 3, 0)#,

        pyxel.blt(107, 62, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(109, 62, 0, 16, 16, 2, 8, 0)#l

        pyxel.blt(114, 64, 0, 62, 2, 5, 6, 0)#v
        pyxel.blt(120, 62, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(122, 62, 0, 21, 24, 5, 8, 0)#t

        pyxel.blt(130, 64, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(136, 64, 0, 27, 18, 5, 6, 0)#n

        pyxel.blt(144, 64, 0, 58, 18, 5, 6, 0)#c
        pyxel.blt(150, 62, 0, 46, 16, 6, 8, 0)#h
        pyxel.blt(156, 61, 0, 72, 8, 5, 9, 0)#â
        pyxel.blt(162, 62, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(168, 64, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(174, 64, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(180, 64, 0, 21, 18, 5, 6, 0)#u

        pyxel.blt(189, 64, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(195, 62, 0, 21, 24, 5, 8, 0)#t

        pyxel.blt(44, 73, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(50, 72, 0, 16, 24, 5, 9, 0)#é
        pyxel.blt(56, 75, 0, 58, 18, 5, 6, 0)#c
        pyxel.blt(62, 73, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(64, 73, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(70, 75, 0, 26, 26, 5, 6, 0)#a

        pyxel.blt(78, 73, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(84, 75, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(92, 75, 0, 40, 26, 5, 6, 0)#s
        pyxel.blt(98, 73, 0, 65, 18, 2, 3, 0)#'
        pyxel.blt(101, 75, 0, 68, 2, 5, 6, 0)#y

        pyxel.blt(109, 75, 0, 60, 10, 5, 6, 0)#r
        pyxel.blt(115, 72, 0, 16, 24, 5, 9, 0)#é
        pyxel.blt(121, 73, 0, 32, 24, 3, 8, 0)#f
        pyxel.blt(125, 75, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(131, 75, 0, 58, 26, 5, 6, 0)#g
        pyxel.blt(137, 73, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(139, 75, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(145, 75, 0, 60, 10, 5, 6, 0)#r

        pyxel.blt(153, 73, 0, 64, 24, 3, 8, 0)#(
        pyxel.blt(157, 75, 0, 40, 26, 5, 6, 0)#s
        pyxel.blt(163, 75, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(169, 75, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(175, 75, 0, 40, 26, 5, 6, 0)#s

        pyxel.blt(183, 75, 0, 40, 26, 5, 6, 0)#s
        pyxel.blt(189, 75, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(195, 75, 0, 62, 2, 5, 6, 0)#v
        pyxel.blt(201, 75, 0, 35, 26, 5, 6, 0)#o
        pyxel.blt(207, 73, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(209, 75, 0, 60, 10, 5, 6, 0)#r

        pyxel.blt(44, 86, 0, 58, 18, 5, 6, 0)#c
        pyxel.blt(50, 86, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(58, 86, 0, 54, 10, -5, 9, 0)#q
        pyxel.blt(64, 86, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(70, 84, 0, 19, 16, 1, 8, 0)#i

        pyxel.blt(74, 84, 0, 16, 16, 2, 8, 0)#l
        pyxel.blt(77, 84, 0, 65, 18, 2, 3, 0)#'
        pyxel.blt(80, 86, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(86, 84, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(92, 84, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(98, 86, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(104, 86, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(110, 84, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(116, 86, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(122, 84, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(124, 84, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(130, 84, 0, 69, 24, 3, 8, 0)#)
        pyxel.blt(134, 91, 0, 69, 20, 1, 1, 0)#.


    def souris(self, etat):
        """La fonction fait apparaitre ou disparaitre la souris"""
        pyxel.mouse(etat)
App()


















