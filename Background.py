from Picture import *

class Background(Picture):
    def __init__(self, screen, x=0, y=0):
        self.img_path = 'images/background.png'
        super().__init__(screen, self.img_path, x=x, y=y)
        self._Picture__img = pygame.transform.scale(self._Picture__img, (400, 600))
