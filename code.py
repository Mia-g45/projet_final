import pyxel


class App:
    def __init__(self):
        pyxel.init(240, 140, title="phantom castle", fps=60)
        pyxel.load("images.pyxres")
        self.couleur_fond = 0
        self.etat = "titre" #etat de l'écran
        self.temps = pyxel.frame_count #sert à stocker la valeur du temps, sera ensuite modifié pour faire des calcules
        pyxel.run(self.update, self.draw)
        pyxel.show() #si on appuie sur la touche echap la fenêtre se ferme


    def update(self):

        if pyxel.btn(pyxel.KEY_SPACE): #la touche espace permet de modifier l'affichage de l'écran
            if self.etat == "titre" and pyxel.frame_count - self.temps > 10: #nettoyer l'écran aprés le titre
                self.etat = "texte"
                self.couleur_fond = 0
                self.apparition_souris()
                self.temps = pyxel.frame_count
            elif self.etat == "texte" and pyxel.frame_count - self.temps > 10: #nettoyer l'écran aprés le texte
                self.couleur_fond = 0
                self.etat = "chateau"



    def draw(self):
        pyxel.cls(self.couleur_fond)
        if self.etat == "titre": #afficher l'image avec le titre
            self.cadre()
            self.titre()
        if self.etat == "texte":
            self.texte()
        if self.etat == "chateau": #afficher l'image avec le chateau
            self.chateau()

    def cadre(self):
        """La fonction dessine le cadre."""
        for x in range(pyxel.width):
            for y in range(pyxel.height):
                if x <= 2 or x >= pyxel.width-3 or y <= 2 or y >= pyxel.height-3:
                    pyxel.pset(x, y, 4)
        pyxel.blt(2, 122, 0, 0, 16, 16, 16, 0) #coin bas gauche
        pyxel.blt(2, 2, 0, 0, 16, 16, -16, 0) #coin haut gauche
        pyxel.blt(222, 122, 0, 0, 16, -16, 16, 0) #coin bas droit
        pyxel.blt(222, 2, 0, 0, 16, -16, -16, 0) #coin haut droit

    def titre(self):
        """écrit le titre du projet"""
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
        pyxel.blt(50, 70, 1, 0, 0, 25, 70, 0)
        pyxel.blt(164, 70, 1, 0, 0, 25, 70, 0)
        pyxel.blt(75, 40, 1, 32, 0, 90, 101, 0)

    def texte(self):
        self.couleur_fond = 0
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

        pyxel.blt(44, 53, 0, 54, 10, 5, 6, 0)#p
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
        pyxel.blt(85, 62, 0, 52, 16, 5, 8, 0)#b
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

        pyxel.blt(10, 10, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(10, 10, 0, 21, 24, 5, 8, 0)#t

        pyxel.blt(10, 10, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(10, 10, 0, 16, 24, 5, 9, 0)#é
        pyxel.blt(10, 10, 0, 58, 18, 5, 6, 0)#c
        pyxel.blt(10, 10, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(10, 10, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(10, 10, 0, 26, 26, 5, 6, 0)#a

        pyxel.blt(10, 10, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(10, 10, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(10, 10, 0, 40, 26, 5, 6, 0)#s
        pyxel.blt(10, 10, 0, 65, 18, 2, 3, 0)#'
        pyxel.blt(10, 10, 0, 68, 2, 5, 6, 0)#y

        pyxel.blt(10, 10, 0, 60, 10, 5, 6, 0)#r
        pyxel.blt(10, 10, 0, 16, 24, 5, 9, 0)#é
        pyxel.blt(10, 10, 0, 32, 24, 3, 8, 0)#f
        pyxel.blt(10, 10, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(10, 10, 0, 58, 26, 5, 6, 0)#g
        pyxel.blt(10, 10, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(10, 10, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(10, 10, 0, 60, 10, 5, 6, 0)#r

        pyxel.blt(10, 10, 0, 64, 24, 3, 8, 0)#(
        pyxel.blt(10, 10, 0, 40, 26, 5, 6, 0)#s
        pyxel.blt(10, 10, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(10, 10, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(10, 10, 0, 40, 26, 5, 6, 0)#s

        pyxel.blt(10, 10, 0, 40, 26, 5, 6, 0)#s
        pyxel.blt(10, 10, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(10, 10, 0, 62, 2, 5, 6, 0)#v
        pyxel.blt(10, 10, 0, 35, 26, 5, 6, 0)#o
        pyxel.blt(10, 10, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(10, 10, 0, 60, 10, 5, 6, 0)#r

        pyxel.blt(10, 10, 0, 58, 18, 5, 6, 0)#c
        pyxel.blt(10, 10, 0, 33, 18, 5, 6, 0)#e

        pyxel.blt(10, 10, 0, 54, 10, 5, -6, 0)#q
        pyxel.blt(10, 10, 0, 21, 18, 5, 6, 0)#u
        pyxel.blt(10, 10, 0, 19, 16, 1, 8, 0)#i

        pyxel.blt(10, 10, 0, 16, 16, 2, 8, 0)#l
        pyxel.blt(10, 10, 0, 65, 18, 2, 3, 0)#'
        pyxel.blt(10, 10, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(10, 10, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(10, 10, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(10, 10, 0, 33, 18, 5, 6, 0)#e
        pyxel.blt(10, 10, 0, 27, 18, 5, 6, 0)#n
        pyxel.blt(10, 10, 0, 52, 24, 5, 8, 0)#d
        pyxel.blt(10, 10, 0, 26, 26, 5, 6, 0)#a
        pyxel.blt(10, 10, 0, 19, 16, 1, 8, 0)#i
        pyxel.blt(10, 10, 0, 21, 24, 5, 8, 0)#t
        pyxel.blt(10, 10, 0, 69, 24, 3, 8, 0)#)
        pyxel.blt(10, 10, 0, 69, 20, 1, 1, 0)#.


    def apparition_souris(self):
        pyxel.mouse(True)
App()



















