import pyxel
import random

class App:

    def __init__(self):
        pyxel.init(240, 140, title="phantom castle", fps=50, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("images.pyxres") #charger l'image
        self.etat = "prison" #le stade du jeu
        self.temps = pyxel.frame_count #sert à stocker la valeur du temps, sera ensuite modifié pour faire des calculs
        self.coordonnee_perso = [20, 95] #coordonnées du personnage
        self.vitesse_perso = 1#vitesse du personnage
        #tableau représentant l'etat du labyrinthe, coupé en une grille de bloc de 5 par 5, chaque couple  ((0 : pas de bloc, 1 : un bloc), nombre de bloc d'affiler avec cet etat), 1 représente le couple (1, 1), 2 représente le couple (0, 2)
        self.tab_labyrinthe = [[(0,20),1,2,1,(0,16),1,(0,7)], [(0,20),1,2,1,(0,16),1,(0,7)], [2,(1,13),(0,5),1,2,1,2,(1,8),2,(1,5),2,(1,2),(0,3)], [2, 1,(0,8),1,2,1,2,(1,4),2,1,2,(1,3),(0,15),1,(0,3)], [2,1,(0,8),1,2,1,2,1,(0,5),1,(0,4),1,(0,15),1,(0,3)], [2,1,2,(1,4),2,1,2,1,2,1,(0,5),1,(0,4),(1,3),2,(1,5),2,(1,5),(0,3)], [2,1,2,1,2,1,2,1,2,1,2,1,2,(1,6),2,1,(0,8),1,2,1,2,1,(0,4)], [(0,5),1,2,1,2,1,2,1,(0,7),1,(0,5),1,(0,8),1,2,1,2,1,2,(1,2)], [(0,5),1,2,1,2,1,2,1,(0,7),1,(0,5),1,2,(1,4),2,1,2,1,2,1,(0,4)], [(1,3),2,1,(0,5),1,2,(1,6),2,1,2,(1,4),2,1,(0,5),1,2,1,2,1,(0,4)], [(0,5),1,(0,5),1,(0,7),1,2,1,(0,8),1,(0,5),(1,4),2,(1,3),(0,2)], [(0,5),1,2,1,2,1,(0,7),1,2,1,(0,8),1,2,1,2,1,(0,7),1,(0,2)], [2,1,2,1,2,1,2,1,2,(1,6),2,1,2,(1,4),2,1,2,1,2,1,(0,7),1,(0,2)], [2,1,2,1,2,1,2,1,(0,4),1,(0,5),1,2,1,(0,5),1,2,(1,4),2,(1,3),2,1,(0,2)], [2,1,2,1,2,1,2,1,(0,4),1,(0,5),1,2,1,(0,5),1,(0,8),(1,3),2,1,(0,2)], [(1,3),2,1,2,1,2,(1,3),2,1,2,(1,4),2,1,2,(1,4),(0,8),(1,3),2,1,(0,2)], [(0,8),1,2,1,(0,4),1,2,1,(0,5),1,2,(1,15),2,1,(0,2)], [(0,8),1,2,1,(0,4),1,2,1,(0,5),1,(0,16),1,2,1,(0,2)], [2,(1,7),2,1,2,(1,3),2,(1,7),(0,16),1,2,1,(0,2)], [2,1,(0,8),1,(0,17),(1,14),2,1,(0,2)], [2,1,(0,8),1,(0,17),1,(0,15),1,(0,2)], [2,1,2,(1,9),2,(1,8),2,(1,4),(0,15),1,(0,2)], [2,1,(0,10),1,2,1,(0,9),1,2,1,2,(1,14),(0,2)], [2,1,(0,10),1,2,1,(0,9),1,2,1,(0,15),1,(0,2)], [2,(1,6),2,1,2,1,2,1,2,(1,5),2,1,2,1,(0,15),1,(0,2)], [2,1,(0,7),1,2,1,2,1,2,(1,5),2,1,2,1,2,(1,8),2,1,2,1,(0,2)], [2,1,(0,7),1,(0,5),1,(0,12),1,2,1,(0,9),1,(0,5)], [2,1,(0,7),1,(0,5),1,(0,12),1,2,1,(0,9),1,(0,5)]]
        #construction du tableau avec tout les 0 et les 1
        t_labyrinthe = []
        for ligne in self.tab_labyrinthe:
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
            t_labyrinthe.append(tab)
        self.tab_labyrinthe = t_labyrinthe
        self.tab_code = [] #utilisé pour stocker et vérifier si le code saisit par le joueur est correct
        self.chrono = [5, 0] #temps total pour finir le jeu
        self.temps_prison = [1, 0] #temps total pour sortir de la prison
        self.temps_labyrinthe = [1, 30] #temps total pour sortir du labyrinthe
        self.vie = True #sert à savoir si le joueur est encore en vie
        self.etat_aide = False #afficher ou non la fenêtre avec les actions qu'on peut faire
        self.livre = 0
        self.objet = []
        self.i_conversation = 0

        pyxel.run(self.update, self.draw)


    def update(self):
        if self.etat == "titre" and pyxel.frame_count - self.temps > 150: #changer l'écran après le titre
            self.etat = "texte"
            pyxel.cls(0)
            self.temps = pyxel.frame_count

        elif self.etat == "texte" and pyxel.frame_count - self.temps > 600: #changer l'écran après le texte
            pyxel.cls(0)
            self.etat = "chateau"
            self.temps = pyxel.frame_count

        elif self.etat == "chateau" and pyxel.frame_count - self.temps > 100: #changer l'écran après le chateau
            pyxel.cls(0)
            self.etat = "entrer dans le chateau"
            self.temps = pyxel.frame_count
            self.souris(True)

        if self.etat in ["couloir", "prison", "salle 2", "salle 1"]: #pouvoir déplacer le personnage
            if pyxel.btn(pyxel.KEY_LEFT) and self.coordonnee_perso[0] > 0: #le personnage va à gauche, mais ne peut pas sortir de la fenêtre d'affichage
                self.coordonnee_perso[0] = self.coordonnee_perso[0] - self.vitesse_perso

            if pyxel.btn(pyxel.KEY_RIGHT) and self.coordonnee_perso[0] < 222: #le personnage va à droite, mais ne peut pas sortir de la fenêtre d'affichage
                self.coordonnee_perso[0] = self.coordonnee_perso[0] + self.vitesse_perso


        if self.etat == "entrer dans le chateau": #pouvoir déplacer le personnage
            if pyxel.btn(pyxel.KEY_LEFT) and self.coordonnee_perso[0] > 0: #le personnage va à gauche, mais ne peut pas sortir de la fenêtre d'affichage
                self.coordonnee_perso[0] = self.coordonnee_perso[0] - self.vitesse_perso

            if pyxel.btn(pyxel.KEY_RIGHT) and self.coordonnee_perso[0] < 235: #le personnage va à droite, mais ne peut pas sortir de la fenêtre d'affichage
                self.coordonnee_perso[0] = self.coordonnee_perso[0] + self.vitesse_perso

            if self.coordonnee_perso[0] >= 235: #si le personnage 'sort' à droite, il rentre dans le chateau
                self.temps = pyxel.frame_count
                self.etat = "grille"
                self.souris(False)
            if self.coordonnee_perso[0] < 5: #si le personnage 'sort' à gauche, il meurt
                self.etat = "mort foret"
                self.vie = False

        if self.etat == "couloir":
            if pyxel.btn(pyxel.KEY_RETURN) and self.coordonnee_perso[0] > 95 and self.coordonnee_perso[0] < 115: #si on appuie sur la touche entrée quand le personnage se trouve sur la porte avec le numéro 8, le personnage entre dans le labyrinthe
                self.etat = "labyrinthe"
                self.coordonnee_perso = [154, 135] #coordonnées du personnage dans le labyrinthe
            if pyxel.btn(pyxel.KEY_RETURN) and self.coordonnee_perso[0] > 53 and self.coordonnee_perso[0] < 75: #si on appuie sur la touche entrée quand le personnage se trouve sur la porte avec le numéro 6, le personnage entre dans la pièce
                self.etat = "salle 2"
            if pyxel.btn(pyxel.KEY_RETURN) and self.coordonnee_perso[0] > 11 and self.coordonnee_perso[0] < 33 and self.temps + 10 < pyxel.frame_count:#si on appuie sur la touche entrée quand le personnage se trouve sur la porte avec le numéro 18, le personnage peut tenter d'ouvrir la porte avec un code
                self.etat = "salle 1 fermé"
                self.temps = pyxel.frame_count

        if self.etat == "labyrinthe": #déplacer le personnage dans le labyrinthe
            if pyxel.btn(pyxel.KEY_LEFT) and self.coordonnee_perso[0] > 3: #gauche
                if self.tab_labyrinthe[self.coordonnee_perso[1]//5][(self.coordonnee_perso[0]-4)//5] == 1: #il y a un mur
                    self.coordonnee_perso[0] = self.coordonnee_perso[0]
                else: #il n'y a pas de mur
                    self.coordonnee_perso[0] = self.coordonnee_perso[0] - 1

            if pyxel.btn(pyxel.KEY_RIGHT) and self.coordonnee_perso[0] < 236: #droite
                if self.tab_labyrinthe[self.coordonnee_perso[1]//5][(self.coordonnee_perso[0]+4)//5] == 1 : #il y a un mur
                    self.coordonnee_perso[0] = self.coordonnee_perso[0]
                else: #il n'y a pas de mur
                    self.coordonnee_perso[0] = self.coordonnee_perso[0] + 1

            if pyxel.btn(pyxel.KEY_UP) and self.coordonnee_perso[1] > 3: #haut
                if self.tab_labyrinthe[(self.coordonnee_perso[1]-4)//5][self.coordonnee_perso[0]//5] == 1: #il y a un mur
                    self.coordonnee_perso[1] = self.coordonnee_perso[1]
                else: #il n'y a pas de mur
                    self.coordonnee_perso[1] = self.coordonnee_perso[1] - 1

            if pyxel.btn(pyxel.KEY_DOWN) and self.coordonnee_perso[1] < 136: #bas
                if self.tab_labyrinthe[(self.coordonnee_perso[1]+4)//5][self.coordonnee_perso[0]//5] == 1: #il y a un mur
                    self.coordonnee_perso[1] = self.coordonnee_perso[1]
                else: #il n'y a pas de mur
                    self.coordonnee_perso[1] = self.coordonnee_perso[1] + 1

            if self.coordonnee_perso[1] < 9 and self.coordonnee_perso[0] > 105 and self.coordonnee_perso[0] < 112: #première sortie
                self.etat = "mort labyrinthe"
                self.vie = False

            if self.coordonnee_perso[1] > 131 and self.coordonnee_perso[1] < 137 and self.coordonnee_perso[0] < 9: #deuxième sortie
                self.etat = "couloir"
                self.coordonnee_perso = [103, 92] #mettre le personnage devant la porte du labyrinthe quand il sort



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
        elif self.etat == "mort foret": #le personnage meurt de froid dans la forêt
            self.cadre()
            pyxel.blt(115, 100, 0, 35, 104, 10, 16, 0)
            pyxel.text(30, 55, "Malheureusement vous vous etes toujours perdu.", 7)
            pyxel.text(47, 65, "Apres plusieurs heures de marche", 7)
            pyxel.text(45, 75, "vous finissez par mourir de froid.", 7)
        elif self.etat == "grille": #affiche la grille, on voit le personnage entrer dans le chateau
            pyxel.cls(0)
            self.ouverture_grille(self.temps)
        elif self.etat == "prison": #affiche la prison (pas encore fini)
            self.prison()
        elif self.etat == "couloir": #affiche le couloir
            self.couloir()
        elif self.etat == "papier salle 2": #le papier avec les indices pour ouvrir la porte
            self.indice_salle_2()
        elif self.etat == "labyrinthe": #affiche le labyrinthe
            self.labyrinthe()
        elif self.etat == "salle 2": #la salle numéro 6
            self.salle_2()
        elif self.etat == "salle 1 fermé": #la salle numéro 18 est fermé, il faut un code pour l'ouvrir
            self.couloir()
            self.ouverture_porte()
        elif self.etat == "salle 1": #la salle numéro 18 est ouverte
            self.salle_1()
        elif self.etat == "mort labyrinthe": #le personnage prend la mauvaise sortie et meurt
            self.cadre()
            pyxel.blt(115, 100, 0, 35, 104, 10, 16, 0)
            pyxel.text(65, 60, "Vous etes tombe dans un trou.", 7)
            pyxel.text(57, 70, "Vous avez fait une chute mortelle.", 7)
        elif self.etat == "mort chrono": #le personnage n'a pas réussi à sortir dans les temps et il meurt
            self.cadre()
            pyxel.blt(115, 100, 0, 35, 104, 10, 16, 0)
            pyxel.text(65, 60, "Vous avez mis trop de temps.", 7)
            pyxel.text(40, 70, "Vous finissez par mourir dans ce chateau.", 7)
        elif self.etat == "corde": #le personnage essai de s'évader de la prison grâce à la corde
            self.cadre()
            self.evasion()
        elif self.etat == "mort labyrinthe temps": #le personnage n'a pas eu le temps de sortir du labyrinthe et meurt
            self.cadre()
            pyxel.blt(115, 100, 0, 35, 104, 10, 16, 0)
            pyxel.text(65, 60, "Vous avez mis trop de temps.", 7)
            pyxel.text(40, 70, "Vous finissez par mourir dans ce chateau.", 7)
        elif self.etat == "mort prison temps": #le personnage n'a pas eu le temps de sortir de la prison et meurt
            self.cadre()
            pyxel.blt(115, 100, 0, 35, 104, 10, 16, 0)
            pyxel.text(35, 60, "Vous n'avez pas reussi a sortir de la prison.", 7)
            pyxel.text(25, 70, "Vous finissez par mourir de faim dans ce chateau.", 7)
        elif self.etat == "liberté prison" or self.etat == "liberté prison mort":
            self.cadre()
            pyxel.text(62, 50, "La corde etait assez solide.", 7)
            pyxel.text(40, 60, "Tu reussi donc a t'echapper du chateau.", 7)
            if self.etat == "liberté prison mort":
                pyxel.blt(115, 100, 0, 35, 104, 10, 16, 0)
                pyxel.text(7, 70, "Malheureusement tu fini par mourir de faim dans la foret.", 7)
            else:
                pyxel.text(30, 70, "Et tu reussi aussi a rentrer chez toi en vie.", 7)
        elif self.etat == "prison mort":
            self.cadre()
            pyxel.blt(115, 100, 0, 35, 104, 10, 16, 0)
            pyxel.text(30, 60, "Malheureusement la corde etait trop fragile.", 7)
            pyxel.text(20, 70, "Elle s'est cassee et tu a fait un chute mortelle.", 7)
        elif self.etat == "découverte":
            pyxel.cls(0)
            pyxel.text(50, 65, "Il y a un squelette dans le coffre,", 7)
            pyxel.text(70, 75, "c'est celui d'un enfant.", 7)
            if self.temps + 250 < pyxel.frame_count:
                self.etat = "discution"
                self.temps = pyxel.frame_count

        elif self.etat == "discution":
            self.conversation()

        if self.etat not in ["titre", "texte", "chateau", "corde", "mort prison temps", "mort labyrinthe temps"] and self.vie == True: #affiche le chronomètre et l'aide
            self.chronometre()
            self.aide()

    def conversation(self):
        pyxel.cls(0)
        pyxel.blt(20, 92, 0, 0, 56, 18, 48, 8)
        if self.i_conversation == 0 and pyxel.frame_count < self.temps + 20:
            #pyxel.blt(100, 92, 0, 0, 120, 28, 22, 8)
            pyxel.blt(100, 124, 0, 0, 104, 32, 16, 0)
        elif self.i_conversation == 0 and pyxel.frame_count < self.temps + 50:
            pyxel.blt(100, 113, 0, 24, 120, 32, 16, 0)
            pyxel.blt(103, 120, 0, 0, 120, 24, 22, 8)
            pyxel.blt(100, 129, 0, 0, 109, 32, 11, 0)
        elif self.i_conversation == 0 and pyxel.frame_count < self.temps + 100:
            pyxel.blt(100, 113, 0, 24, 120, 32, 16, 0)
            pyxel.blt(103, 110, 0, 0, 120, 24, 22, 8)
            pyxel.blt(100, 129, 0, 0, 109, 32, 11, 0)
        elif self.i_conversation == 0 and pyxel.frame_count < self.temps + 150:
            pyxel.blt(100, 113, 0, 24, 120, 32, 16, 0)
            pyxel.blt(103, 100, 0, 0, 120, 24, 22, 8)
            pyxel.blt(100, 129, 0, 0, 109, 32, 11, 0)
        elif self.i_conversation == 0 and pyxel.frame_count < self.temps + 1200:
            #pyxel.blt(100, 113, 0, 24, 120, 32, 16, 0)
            pyxel.blt(103, 100, 0, 0, 120, 24, 22, 8)
            pyxel.blt(100, 124, 0, 0, 104, 32, 16, 0)


    def salle_1(self):
        self.mur_fond_brique()
        pyxel.blt(145, 79, 1, 0, 112, 32, 64, 0)#porte
        pyxel.blt(200, 100, 0, 50, 63, 21, 9, 0)#étagère
        pyxel.blt(20, 124, 0, 0, 104, 32, 16, 0)#coffre
        if "clé" in self.objet:
            pyxel.blt(self.coordonnee_perso[0] + 4, 65, 0, 52, 75, 50, 50, 0)
        if pyxel.btn(pyxel.KEY_RETURN) and self.coordonnee_perso[0] > 145 and self.coordonnee_perso[0] < 160 and self.temps + 10 < pyxel.frame_count: #si on appuie sur la touche entrée quand le personnage se trouve sur la porte, le personnage sort de la pièce
            self.etat = "couloir"
            self.coordonnee_perso = [20, 92]
            self.temps = pyxel.frame_count
        if self.coordonnee_perso[0] > 190 and self.coordonnee_perso[0] < 225:
            if "clé" not in self.objet:
                pyxel.text(162, 62, "On dirais une boite", 7)
                pyxel.text(160, 68, "appuie sur la touche", 7)
                pyxel.text(159, 74, "entree pour recuperer", 7)
                pyxel.text(195, 80, "la cle", 7)
            if pyxel.btn(pyxel.KEY_RETURN):
                self.objet.append("clé")
        if self.coordonnee_perso[0] > 15 and self.coordonnee_perso[0] < 40 and "clé" in self.objet and pyxel.btn(pyxel.KEY_RETURN):
            self.objet = []
            self.etat = "découverte"
            self.temps = pyxel.frame_count
            self.vie = False
        pyxel.blt(self.coordonnee_perso[0], 92, 0, 0, 56, 18, 48, 8)

    def salle_2(self):
        self.mur_fond_brique()
        pyxel.blt(100, 76, 0, 18, 40, 31, 64, 0)#bibliothèque
        pyxel.blt(30, 79, 1, 0, 112, 32, 64, 0)#porte
        pyxel.blt(4, 90, 0, 50, 40, 22, 21, 0)#poster
        pyxel.blt(170, 85, 1, 32, 120, 48, 24, 8)#tableau
        if self.coordonnee_perso[0] > 200 and self.coordonnee_perso[0] < 215 and pyxel.btn(pyxel.KEY_RETURN) and self.temps + 10 < pyxel.frame_count:
            self.etat = "papier salle 2"
            self.temps = pyxel.frame_count
        if self.coordonnee_perso[0] < 25:
            pyxel.text(1, 60, "On dirais", 7)
            pyxel.text(1, 66, "un arbre", 7)
            pyxel.text(1, 72, "genealogique", 7)
        pyxel.blt(self.coordonnee_perso[0], 92, 0, 0, 56, 18, 48, 8)
        if self.coordonnee_perso[0] > 95 and self.coordonnee_perso[0] < 120:
            if pyxel.btn(pyxel.KEY_RETURN) and self.temps + 10 < pyxel.frame_count:
                if self.livre == 0:
                    self.livre = 1
                    self.temps = pyxel.frame_count
                elif self.livre == 1:
                    self.livre = 2
                    self.temps = pyxel.frame_count
                elif self.livre == 2:
                    self.livre = 3
                    self.temps = pyxel.frame_count
                elif self.livre == 3:
                    self.livre = 4
                    self.temps = pyxel.frame_count
                elif self.livre == 4:
                    self.livre = 0
                    self.temps = pyxel.frame_count


            if self.livre == 1:
                pyxel.rect(80, 20, 85, 100, 15)
                pyxel.text(85, 30, "page 27", 13)
                pyxel.text(85, 40, "Journal intime", 13)
                pyxel.text(85, 50, "Louis", 13)
                pyxel.text(85, 60, "15/02/1868", 13)
                pyxel.text(85, 70, "J'ai peur.", 13)
                pyxel.text(85, 80, "Aujourd'hui Jean", 13)
                pyxel.text(85, 90, "m'a enferme dans", 13)
                pyxel.text(85, 100, "le coffre a jouet.", 13)
                pyxel.text(85, 110, "J'y ai passe 3h.", 13)
            if self.livre == 2:
                pyxel.rect(80, 20, 85, 100, 15)
                pyxel.text(85, 30, "page 28", 13)
                pyxel.text(85, 40, "17/02/1868", 13)
                pyxel.text(85, 50, "Il a recomence.", 13)
                pyxel.text(85, 60, "J'ai ete enferme", 13)
                pyxel.text(85, 70, "durant toute la nuit", 13)
                pyxel.text(85, 80, "Je l'ai entendu", 13)
                pyxel.text(85, 90, "ranger la cle dans", 13)
                pyxel.text(85, 100, "une boite.", 13)
                #pyxel.text(85, 110, "-------------------", 13)
            if self.livre == 3:
                pyxel.rect(80, 20, 85, 100, 15)
                pyxel.text(85, 30, "page 29", 13)
                #pyxel.text(85, 40, "-------------------", 13)
                #pyxel.text(85, 50, "-------------------", 13)
                #pyxel.text(85, 60, "-------------------", 13)
                #pyxel.text(85, 70, "-------------------", 13)
                #pyxel.text(85, 80, "-------------------", 13)
                #pyxel.text(85, 90, "-------------------", 13)
                #pyxel.text(85, 100, "-------------------", 13)
                #pyxel.text(85, 110, "-------------------", 13)
            if self.livre == 4:
                pyxel.rect(80, 20, 85, 100, 15)
                pyxel.text(85, 30, "page 30", 13)
                #pyxel.text(85, 40, "-------------------", 13)
                #pyxel.text(85, 50, "-------------------", 13)
                #pyxel.text(85, 60, "-------------------", 13)
                #pyxel.text(85, 70, "-------------------", 13)
                #pyxel.text(85, 80, "-------------------", 13)
                #pyxel.text(85, 90, "-------------------", 13)
                #pyxel.text(85, 100, "-------------------", 13)
                #pyxel.text(85, 110, "-------------------", 13)
        if pyxel.btn(pyxel.KEY_RETURN) and self.coordonnee_perso[0] > 33 and self.coordonnee_perso[0] < 53: #si on appuie sur la touche entrée quand le personnage se trouve sur la porte, le personnage sort de la pièce
            self.etat = "couloir"





    def evasion(self):
        #pas fini
        """Le personnage tente de s'échapper de la prison, il a une chance sur cinq de sortir vivant, sinon la corde casse et il fait une chute mortelle."""
        pyxel.cls(0)
        pyxel.text(15, 40, "Il y a assez de place pour passer entre les barreaux", 7)
        pyxel.text(18, 50, "et on dirais qu'une corde est accrochee au barreau.", 7)
        pyxel.text(55, 60, "Veut-tu tenter de t'echapper ?", 7)
        pyxel.text(32, 80, "Appuie sur la touche entree pour t'echapper", 7)
        pyxel.text(38, 90, "Appuie sur la touche effacer pour rester", 7)
        if pyxel.btn(pyxel.KEY_RETURN) and self.temps + 20 < pyxel.frame_count:
            self.temps = pyxel.frame_count
            if random.choice([True, False]):
                if random.choice([True, False]):
                    self.etat = "liberté prison"
                    self.vie = False
                else:
                    self.etat = "liberté prison mort"
                    self.vie = False
            else:
                self.etat = "prison mort"
                self.vie = False
        if pyxel.btn(pyxel.KEY_BACKSPACE):
            self.etat = "prison"

    def aide(self):
        """Un petit i s'affiche au coin supérieur droit de l'écran, si on clique dessus avec la souris, le joueur peut voir les touches et actions auquels il a accès"""
        pyxel.circ(228, 11, 5, 4) #le cerle
        pyxel.blt(228, 9, 0, 19, 16, 1, 6, 0)#i
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x < 233 and pyxel.mouse_x > 223 and pyxel.mouse_y < 16 and pyxel.mouse_y > 6 and self.temps + 10 < pyxel.frame_count: #clique sur le bouton
            if self.etat_aide == True: #fermer la fenêtre d'aide
                self.etat_aide = False
                self.temps = pyxel.frame_count
            else: #ouvrir la fenêtre d'aide
                self.etat_aide = True
                self.temps = pyxel.frame_count
        if self.etat_aide == True: #afficher la fenêtre d'aide, différente selon le lieu ou se trouve le joueur
            pyxel.rect(70, 30, 100, 80, 0)
            if self.etat in ["prison", "couloir", "salle 2", 'salle 1', "papier salle 2"]:
                pyxel.text(75, 40, '- utiliser les fleches', 7)
                pyxel.text(75, 50, 'de direction pour', 7)
                pyxel.text(75, 60, 'se deplacer', 7)
                pyxel.blt(130, 60, 0, 39, 34, 6, 6, 0) #flèche gauche
                pyxel.blt(140, 60, 0, 32, 34, 6, 6, 0) #flèche droite
                pyxel.text(75, 70, '- utiliser la touche', 7)
                pyxel.text(75, 80, 'entrer pour interagir', 7)
                pyxel.text(75, 90, 'avec un objet', 7)
            if self.etat == "labyrinthe":
                pyxel.text(75, 45, '- utiliser les fleches', 7)
                pyxel.text(75, 55, 'de direction pour', 7)
                pyxel.text(75, 65, 'se deplacer', 7)
                pyxel.blt(105, 87, 0, 39, 34, 6, 6, 0) #flèche gauche
                pyxel.blt(125, 87, 0, 32, 34, 6, 6, 0) #flèche droite
                pyxel.blt(115, 77, 0, 46, 34, 6, 6, 0) #flèche haut
                pyxel.blt(115, 97, 0, 53, 34, 6, 6, 0) #flèche bas
            if self.etat == "entrer dans le chateau":
                pyxel.text(75, 45, '- utiliser les fleches', 7)
                pyxel.text(75, 55, 'de direction pour', 7)
                pyxel.text(75, 65, 'se deplacer', 7)
                pyxel.blt(125, 65, 0, 39, 34, 6, 6, 0) #flèche gauche
                pyxel.blt(135, 65, 0, 32, 34, 6, 6, 0) #flèche droite


    def temps_ecouler(self, attribut):
        """Cette fonction permet de diminuer le temps, pour le chronomètre ou pour les salles avec un temps d'accès limité"""
        if attribut[1] == 0:
            attribut[1] = 59
            attribut[0] = attribut[0] - 1
        attribut[1] = attribut[1] - 1


    def chronometre(self):
        """Permet d'afficher le temps qu'il reste au joueur pour sortir et gère le temps dans les salles à accès limité"""
        pyxel.blt(5, 5, 1, 32, 144, 29, 13, 8)
        if pyxel.frame_count % 55 == 0: #changer le temps à chaque seconde
            pyxel.blt(5, 5, 1, 32, 144, 29, 13, 8)
            self.temps_ecouler(self.chrono)
            if self.etat == "prison":
                self.temps_ecouler(self.temps_prison)
            if self.etat == "labyrinthe":
                self.temps_ecouler(self.temps_labyrinthe)

        #afficher le chronomètre en ajoutant un zéro quand le nombre est inférieur à 10
        if self.chrono[0] < 10:
            if self.chrono[1] < 10:
                pyxel.text(10, 9, '0' + str(self.chrono[0]) + ':0' + str(self.chrono[1]), 4)
            else:
                pyxel.text(10, 9, '0' + str(self.chrono[0]) + ':' + str(self.chrono[1]), 4)
        else:
            if self.chrono[1] < 10:
                pyxel.text(10, 9, str(self.chrono[0]) + ':0' + str(self.chrono[1]), 4)
            else:
                pyxel.text(10, 9, str(self.chrono[0]) + ':' + str(self.chrono[1]), 4)

        if self.chrono == [0, 0]: #le temps de jeu est écoulé
            self.etat = "mort chrono"
            self.vie = False
        if self.temps_prison == [0, 0]: #le temps dans la prison est écoulé
            self.etat = "mort prison temps"
        if self.temps_labyrinthe == [0, 0]: #le temps dans le labyrinthe est écoulé
            self.etat = "mort labyrinthe temps"


    def indice_salle_2(self):
        """Cette fonction affiche le papier caché derrière le tableau dans le couloir"""
        self.mur_fond_brique()
        pyxel.blt(100, 76, 0, 18, 40, 31, 64, 0)#bibliothèque
        pyxel.blt(30, 79, 1, 0, 112, 32, 64, 0)#porte
        pyxel.blt(4, 90, 0, 50, 40, 22, 21, 0)#poster
        pyxel.blt(170, 85, 1, 32, 120, 48, 24, 8)#tableau
        pyxel.blt(self.coordonnee_perso[0], 92, 0, 0, 56, 18, 48, 8)
        pyxel.rect(80, 20, 85, 100, 15)
        pyxel.text(85, 30, "Il y a 157 ans", 13)
        pyxel.text(85, 40, "il y eu un drame", 13)
        pyxel.text(85, 50, "dans ce chateau.", 13)
        pyxel.text(85, 60, "Quelqu'un est mort.", 13)
        pyxel.text(85, 70, "Trouver des indices", 13)
        pyxel.text(85, 80, "pour reconstituer", 13)
        pyxel.text(85, 90, "l'histoire.", 13)
        pyxel.text(85, 100, "le code est :", 13)
        pyxel.text(85, 110, "0001 1000 0110 1000", 13)
        if pyxel.btn(pyxel.KEY_RETURN) and self.temps + 10 < pyxel.frame_count: #reposer le papier
            self.etat = "salle 2"
            self.temps = pyxel.frame_count




    def ouverture_porte(self):
        """Cette fonction permet de rentrer le code de la porte et s'il est correct le joueur peut entrer dans la salle"""
        pyxel.rect(70, 32, 100, 60, 0)
        pyxel.text(92, 50, "entrer le code", 7)
        pyxel.line(101, 75, 107, 75, 7)
        pyxel.line(111, 75, 117, 75, 7)
        pyxel.line(121, 75, 127, 75, 7)
        pyxel.line(131, 75, 137, 75, 7)
        if len(self.tab_code) < 4:
            if self.temps + 10 < pyxel.frame_count:
                if (pyxel.btn(pyxel.KEY_0) or pyxel.btn(pyxel.KEY_KP_0)):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(0)
                elif pyxel.btn(pyxel.KEY_1) or pyxel.btn(pyxel.KEY_KP_1):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(1)
                elif pyxel.btn(pyxel.KEY_2) or pyxel.btn(pyxel.KEY_KP_2):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(2)
                elif pyxel.btn(pyxel.KEY_3) or pyxel.btn(pyxel.KEY_KP_3):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(3)
                elif pyxel.btn(pyxel.KEY_4) or pyxel.btn(pyxel.KEY_KP_4):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(4)
                elif pyxel.btn(pyxel.KEY_5) or pyxel.btn(pyxel.KEY_KP_5):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(5)
                elif pyxel.btn(pyxel.KEY_6) or pyxel.btn(pyxel.KEY_KP_6):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(6)
                elif pyxel.btn(pyxel.KEY_7) or pyxel.btn(pyxel.KEY_KP_7):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(7)
                elif pyxel.btn(pyxel.KEY_8) or pyxel.btn(pyxel.KEY_KP_8):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(8)
                elif pyxel.btn(pyxel.KEY_9) or pyxel.btn(pyxel.KEY_KP_9):
                    self.temps = pyxel.frame_count
                    self.tab_code.append(9)
        if pyxel.btn(pyxel.KEY_BACKSPACE) and len(self.tab_code) > 0 and self.temps + 10 < pyxel.frame_count: #effecer le dernier chiffre du code
            tab = []
            for i in range(len(self.tab_code)-1):
                tab.append(self.tab_code[i])
            self.tab_code = tab
            self.temps = pyxel.frame_count
        if len(self.tab_code) == 4 and pyxel.btn(pyxel.KEY_RETURN): #tester sa réponse
            if self.tab_code == [1, 8, 6, 8]: #le code est bon
                self.etat = "salle 1"
                self.coordonnee_perso = [155, 92]
                self.temps = pyxel.frame_count
            else: #le code n'est pas bon
                self.temps = pyxel.frame_count
                self.tab_code = []
                self.etat = "couloir"
        for i in range(len(self.tab_code)): #affiche le code saisit par le joueur
            pyxel.text(103 + (i*10), 69, str(self.tab_code[i]), 7)

    def mur_fond_brique(self):
        """Cette fonction dessine un mur de brique sur tout le fond de la fenêtre"""
        pyxel.bltm(0, 0, 0, 0, 0, 64, 128, 0)
        pyxel.bltm(64, 0, 0, 0, 0, 64, 128, 0)
        pyxel.bltm(128, 0, 0, 0, 0, 64, 128, 0)
        pyxel.bltm(192, 0, 0, 0, 0, 48, 128, 0)
        pyxel.bltm(0, 128, 0, 0, 0, 64, 12, 0)
        pyxel.bltm(64, 128, 0, 0, 0, 64, 12, 0)
        pyxel.bltm(128, 128, 0, 0, 0, 64, 12, 0)
        pyxel.bltm(192, 128, 0, 0, 0, 48, 12, 0)

    def prison(self):
        """Cette fonction dessine la prison."""
        self.souris(True)
        self.mur_fond_brique()

        #la fenêtre avec les barreaux
        pyxel.rect(146, 64, 58, 39, 0)
        for x in range(153, 190, 15):
            pyxel.line(x, 64, x, 102, 13)
            pyxel.line(x+1, 64, x+1, 102, 13)
        #le bout de corde accroché à la fenêtre
        pyxel.line(182, 97, 185, 97, 15)
        pyxel.line(182, 98, 185, 98, 15)

        pyxel.blt(self.coordonnee_perso[0], 92, 0, 0, 56, 18, 48, 8) #le personnage

        for x in range(6, 240, 14): #les barreaux de la prison
            pyxel.line(x, 0, x, 140, 7)
            pyxel.line(x+1, 0, x+1, 140, 7)
            pyxel.line(x+2, 0, x+2, 140, 7)

        for y in [20, 56, 89, 120]: #les impérfections sur le deuxième barreau (il est cassé)
            pyxel.pset(20, y, 13)
            pyxel.pset(21, y - 8, 13)
            pyxel.pset(22, y + 10, 13)

        if self.coordonnee_perso[0] < 28 and self.coordonnee_perso[0] > 10 and pyxel.btn(pyxel.KEY_RETURN): #le joueur s'échappe par le barreaux cassé
            self.etat = "couloir"
            self.coordonnee_perso = [210, 92] #coordonnées du personnage dans le couloir 117

        if self.coordonnee_perso[0] < 190 and self.coordonnee_perso[0] > 170 and pyxel.btn(pyxel.KEY_RETURN): #le joueur s'échappe par la corde
            self.etat = "corde"
            self.temps = pyxel.frame_count
            self.souris(False)

    def labyrinthe(self):
        """Cette fonction dessine le labyrinthe et permet au personnage de se déplacer."""
        pyxel.cls(13)
        #afficher le labyrinthe
        for i_ligne in range(len(self.tab_labyrinthe)):
            for i_colonne in range(len(self.tab_labyrinthe[i_ligne])):
                if self.tab_labyrinthe[i_ligne][i_colonne] == 1:
                    pyxel.blt(i_colonne*5, i_ligne*5, 1, 40, 112, 5, 5, 0)
        pyxel.rect(105, 0, 10, 10, 0) #la sortie en haut
        pyxel.rect(0, 130, 10, 10, 0) #la sortie en bas
        pyxel.blt(107, 12, 0, 46, 34, 6, 6, 0) #flèche haut
        pyxel.blt(2, 122, 0, 53, 34, 6, 6, 0) #flèche bas
        pyxel.circ(self.coordonnee_perso[0], self.coordonnee_perso[1], 3, 4) #le personnage


    def couloir(self):
        """Cette fonction dessine le couloir avec les trois porte. Si bool est égal à True le joueur pourra effectuer des action dans le couloir, sinon la fonction dessinera juste le couloir"""
        self.mur_fond_brique()
        pyxel.blt(10, 79, 1, 0, 112, 32, 64, 0)#porte 1
        pyxel.blt(52, 79, 1, 0, 112, 32, 64, 0)#porte 2
        pyxel.blt(94, 79, 1, 0, 112, 32, 64, 0)#porte 3
        pyxel.blt(22, 94, 0, 18, 35, 2, 5, 0)#1
        pyxel.blt(26, 94, 0, 21, 35, 4, 5, 0)#8
        pyxel.blt(66, 94, 0, 26, 35, 4, 5, 0)#6
        pyxel.blt(108, 94, 0, 21, 35, 4, 5, 0)#8
        pyxel.text(99, 85, "Danger", 13)#attention porte 3
        pyxel.blt(160, 85, 1, 32, 120, 43, 24, 8)#tableau
        if self.coordonnee_perso[0] > 11 and self.coordonnee_perso[0] < 33 and self.tab_code != [1, 8, 6, 8]:
            pyxel.text(1, 60, "La porte est fermee.", 7)
            pyxel.text(1, 66, "Il faut un code a 4 chiffres'", 7)
            pyxel.text(1, 72, "pour l'ouvrir.", 7)
        pyxel.blt(self.coordonnee_perso[0], self.coordonnee_perso[1], 0, 0, 56, 18, 48, 8)
        #if bool:

        #pyxel.blt(self.coordonnee_perso[0], self.coordonnee_perso[1], 0, 0, 33, 9, 23, 8)


    def ouverture_grille(self, temps):
        pyxel.bltm(0, 0, 0, 0, 0, 120, 140) #mur de brique (partie gauche)
        pyxel.bltm(119, 0, 0, 0, 0, -121, 140) #mur de brique (partie droite)

        pyxel.line(70, 140, 70, 70, 0) #ligne gauche de l'encadrement de porte
        pyxel.line(169, 140, 169, 70, 0) #ligne droite de l'encadrement de porte
        pyxel.elli(71, 35, 98, 75,  0) #l'arrondi au dessus de l'encadrement de porte

        y = 140 #change de valeur pour donner l'impression que la grille s'ouvre et se ferme
        endroit = "dehors" #permet d'afficher le personnage devant ou derière la grille
        if pyxel.frame_count < temps + 10:
            y = 140
        elif pyxel.frame_count < temps + 20:
            y = 130
        elif pyxel.frame_count < temps + 30:
            y = 120
        elif pyxel.frame_count < temps + 40:
            y = 110
        elif pyxel.frame_count < temps + 50:
            y = 100
        elif pyxel.frame_count < temps + 60:
            y = 90
        elif pyxel.frame_count < temps + 70:
            y = 80
        elif pyxel.frame_count < temps + 80:
            y = 90
            endroit = "dedans"
        elif pyxel.frame_count < temps + 90:
            y = 100
            endroit = "dedans"
        elif pyxel.frame_count < temps + 100:
            y = 110
            endroit = "dedans"
        elif pyxel.frame_count < temps + 110:
            y = 120
            endroit = "dedans"
        elif pyxel.frame_count < temps + 120:
            y = 130
            endroit = "dedans"
        elif pyxel.frame_count < temps + 130:
            y = 140
            endroit = "dedans"
        elif pyxel.frame_count < temps + 140:
            self.etat = "prison"
            self.coordonnee_perso = [120, 90]
        if self.etat != "prison":
            if endroit == "dedans": #afficher le personnage derrière la grille
                pyxel.blt(113, 92, 0, 0, 56, 18, 48, 8)

            #dessiner tous les barreaux de la grille
            #1
            pyxel.line(73, y - 1, 73, 61, 7)
            pyxel.line(74, y, 74, 59, 7)
            pyxel.line(75, y - 1, 75, 57, 7)
            #2
            pyxel.line(80, y - 1, 80, 50, 7)
            pyxel.line(81, y, 81, 49, 7)
            pyxel.line(82, y - 1, 82, 49, 7)
            #3
            pyxel.line(87, y - 1, 87, 45, 7)
            pyxel.line(88, y, 88, 44, 7)
            pyxel.line(89, y - 1, 89, 43, 7)
            #4
            pyxel.line(94, y - 1, 94, 41, 7)
            pyxel.line(95, y, 95, 40, 7)
            pyxel.line(96, y - 1, 96, 40, 7)
            #5
            pyxel.line(101, y - 1, 101, 38, 7)
            pyxel.line(102, y, 102, 37, 7)
            pyxel.line(103, y - 1, 103, 37, 7)
            #6
            pyxel.line(108, y - 1, 108, 36, 7)
            pyxel.line(109, y, 109, 36, 7)
            pyxel.line(110, y - 1, 110, 36, 7)
            #7
            pyxel.line(115, y - 1, 115, 35, 7)
            pyxel.line(116, y, 116, 35, 7)
            pyxel.line(117, y - 1, 117, 35, 7)
            #8
            pyxel.line(122, y - 1, 122, 35, 7)
            pyxel.line(123, y, 123, 35, 7)
            pyxel.line(124, y - 1, 124, 35, 7)
            #9
            pyxel.line(129, y - 1, 129, 36, 7)
            pyxel.line(130, y, 130, 36, 7)
            pyxel.line(131, y - 1, 131, 36, 7)
            #10
            pyxel.line(136, y - 1, 136, 37, 7)
            pyxel.line(137, y, 137, 37, 7)
            pyxel.line(138, y - 1, 138, 38, 7)
            #11
            pyxel.line(143, y - 1, 143, 40, 7)
            pyxel.line(144, y, 144, 40, 7)
            pyxel.line(145, y - 1, 145, 41, 7)
            #12
            pyxel.line(150, y - 1, 150, 43, 7)
            pyxel.line(151, y, 151, 44, 7)
            pyxel.line(152, y - 1, 152, 45, 7)
            #13
            pyxel.line(157, y - 1, 157, 49, 7)
            pyxel.line(158, y, 158, 49, 7)
            pyxel.line(159, y - 1, 159, 50, 7)
            #14
            pyxel.line(164, y - 1, 164, 57, 7)
            pyxel.line(165, y, 165, 59, 7)
            pyxel.line(166, y - 1, 166, 61, 7)
            if endroit == "dehors": #permet d'afficher le personnage devant la grille
                pyxel.blt(113, 92, 0, 0, 56, 18, 48, 8)



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

        pyxel.blt(self.coordonnee_perso[0], self.coordonnee_perso[1], 0, 0, 33, 9, 23, 8) #le perso


    def cadre(self):
        """La fonction dessine un cadre."""
        pyxel.cls(0)
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