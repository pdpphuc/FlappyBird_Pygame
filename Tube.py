from random import randint

from Picture import *

class Tube(Picture):
    def __init__(self, screen, x=0, y=0):
        self.img_path = 'images/tube.png'
        super().__init__(screen, self.img_path, x=x, y=y)
        self.width = 50
        self.height = randint(100, 400)
        self._Picture__img = pygame.transform.scale(self._Picture__img, (self.width, self.height))
        self.passed = False

    def reset(self):
        super().reset()
        self.height = randint(100, 400)
        self._Picture__img = pygame.transform.scale(self._Picture__img, (self.width, self.height))
        self.passed = False