from Picture import *

class Bird(Picture):
    def __init__(self, screen, x=50, y=350):
        self.img_path = 'images/bird.png'
        super().__init__(screen, self.img_path, x=x, y=y)
        self._Picture__img = pygame.transform.scale(self._Picture__img, (35, 35))