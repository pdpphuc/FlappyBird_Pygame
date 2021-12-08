from Picture import *

class Tube_op(Picture):

    D_2_TUBE = 150

    def __init__(self, screen, tube):
        self.img_path = 'images/tube_op.png'
        super().__init__(screen, self.img_path, x=tube.x, y=tube.height+Tube_op.D_2_TUBE)
        self.tube = tube
        self.width = tube.width
        self.height = pygame.display.get_surface().get_size()[1] - self.y
        self._Picture__img = pygame.transform.scale(self._Picture__img, (self.width, self.height))

    def draw(self):
        self.x = self.tube.x
        self.y = self.tube.height + Tube_op.D_2_TUBE
        self.height = pygame.display.get_surface().get_size()[1] - self.y
        self._Picture__img = pygame.transform.scale(self._Picture__img, (self.width, self.height))
        self._Picture__obj = self._Picture__screen.blit(self._Picture__img, (self.x, self.y))