import pyxel

class App:
    def __init__(self):
        pyxel.init(240, 140, title="Classe App", fps=60)
        pyxel.load("images.pyxres")
        pyxel.run(self.update, self.draw)
        pyxel.show() #si on appuie sur la touche echap la fenêtre se ferme



    def update(self):
        #pyxel.mouse(True)
        pass


    def draw(self):
        #pyxel.cls(0)
        self.cadre_intro()

    def cadre_intro(self):
        """La fonction dessine le cadre de l'intro et y met le textedu debut de l'histoire."""
        for x in range(pyxel.width):
            for y in range(pyxel.height):
                if x <= 2 or x >= pyxel.width-3 or y <= 2 or y >= pyxel.height-3:
                    pyxel.pset(x, y, 4)
        pyxel.blt(2, 122, 0, 0, 0, 16, 16, 0) #coin bas gauche
        pyxel.blt(2, 2, 0, 0, 0, 16, -16, 0) #coin haut gauche
        pyxel.blt(222, 122, 0, 0, 0, -16, 16, 0) #coin bas droit
        pyxel.blt(222, 2, 0, 0, 0, -16, -16, 0) #coin haut droit

        pyxel.blt(15, 35, 0, 16, 0, 6, 8, 0) #P
        pyxel.blt(25, 35, 0, 24, 0, 8, 8, 0) #H
        pyxel.blt(35, 35, 0, 32, 0, 8, 8, 0) #A
        pyxel.blt(45, 35, 0, 40, 0, 8, 8, 0) #N
        pyxel.blt(55, 35, 0, 48, 0, 7, 8, 0) #T
        pyxel.blt(65, 35, 0, 55, 0, 6, 8, 0) #O
        pyxel.blt(75, 35, 0, 16, 8, 9, 8, 0) #M
        pyxel.blt(85, 35, 0, 44, 8, 6, 8, 0) #E

        pyxel.blt(15, 45, 0, 25, 8, 6, 8, 0) #C
        pyxel.blt(25, 45, 0, 32, 0, 8, 8, 0) #A
        pyxel.blt(35, 45, 0, 32, 8, 6, 8, 0) #S
        pyxel.blt(45, 45, 0, 48, 0, 7, 8, 0) #T
        pyxel.blt(55, 45, 0, 38, 8, 6, 8, 0) #L
        pyxel.blt(65, 45, 0, 44, 8, 6, 8, 0) #E
App()