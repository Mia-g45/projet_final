import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 128, title="Classe App", fps=60)
        pyxel.load("images.pyxres")
        pyxel.run(self.update, self.draw)



    def update(self):
        pyxel.mouse(True)
        pyxel.blt(20, 20, 0, 0, 0, 32, 48)

    def draw(self):
        pass


App()