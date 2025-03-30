import pyxel



class App:
    def __init__(self):
        pyxel.init(240, 140, title="phantom castle", fps=60)
        pyxel.load("images.pyxres")
        self.couleur_fond = 0
        self.temps_titre = 100 #temps d'affichage 1ère image
        self.temps_texte = 200 #
        pyxel.run(self.update, self.draw)
        pyxel.show() #si on appuie sur la touche echap la fenêtre se ferme


    def update(self):
        if pyxel.frame_count == self.temps_titre: #nettoyer l'écran aprés le titre
            self.couleur_fond = 5
        if pyxel.frame_count == self.temps_texte: #nettoyer l'écran aprés le texte
            self.couleur_fond = 0
        if pyxel.frame_count == 100: #apparition de la souris au bout d'un certain temps
            self.apparition_souris()



    def draw(self):
        pyxel.cls(self.couleur_fond)
        if pyxel.frame_count < self.temps_titre:
            self.cadre()
            self.titre()
        if pyxel.frame_count > 200:
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
        pyxel.blt(165, 70, 1, 0, 0, 25, 70, 0)

    def apparition_souris(self):
        pyxel.mouse(True)
App()



















