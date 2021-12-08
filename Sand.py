from Picture import *

class Sand(Picture):
    def __init__(self, screen, x=0, y=570):
        self.img_path = 'images/sand.png'
        super().__init__(screen, self.img_path, x=x, y=y)
        self._Picture__img = pygame.transform.scale(self._Picture__img, (800, 30))
