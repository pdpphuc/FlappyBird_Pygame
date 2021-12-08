import pygame
pygame.init()
from time import sleep

from Font import *
from Color import *

from Background import *
from Bird import *
from Tube import *
from Tube_op import *
from Sand import *

class Game_FlappyBird:

    # Âm thanh
    SOUND = pygame.mixer.Sound('music/no6.wav')

    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption('Flappy Bird')
        programIcon = pygame.image.load('images/Flappy_Bird_icon.png')
        pygame.display.set_icon(programIcon)

        self.__background = Background(self.__screen)
        self.__bird = Bird(self.__screen)
        self.__tubes= [Tube(self.__screen, x) for x in range(400, 801, 200)]
        self.__tubes_op= [Tube_op(self.__screen, self.__tubes[i]) for i in range(0, len(self.__tubes))]
        self.__sand = Sand(self.__screen)
        self.__end_point = 0

        self.__score = 0
        self.__score_txt = Font.SANS_25.render(f'Score: {self.__score}', True, Color.RED)
        self.__space_txt = Font.SANS_25.render('Press Space to continue!', True, Color.BLUE)

        self.__running = True
        self.pausing = True
        self.__game_over = False

    def set_pausing_state(self):
        self.__Vx = 0
        self.__Vy = 0
        self.__gravity = 0
        pygame.mixer.pause()

    def set_playing_state(self):
        self.__Vx = 2
        self.__Vy = 0
        self.__gravity = 0.5
        pygame.mixer.Sound.play(Game_FlappyBird.SOUND)

    @property
    def pausing(self):
        return self.__pausing

    @pausing.setter
    def pausing(self, value):
        self.__pausing = value
        if value:
            self.set_pausing_state()
        else:
            self.set_playing_state()

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value
        self.__score_txt = Font.SANS_25.render(f'Score: {self.__score}', True, Color.RED)

    def draw_score(self):
        self.__screen.blit(self.__score_txt, (5, 5))

    def draw_game_over(self):
        self.__game_over_txt = Font.SANS_25.render(f'GAME OVER, Score: {self.score}', True, Color.RED)
        self.__screen.blit(self.__game_over_txt, (85, 260))   
        self.__screen.blit(self.__space_txt, (80, 290))
        pygame.display.flip()

    def draw_instruction(self):
        self.__screen.blit(self.__space_txt, (80, 290))
        pygame.display.flip()

    def check_bird_colliderect_objects(self):
        for tube in self.__tubes:
            if self.__bird._Picture__obj.colliderect(tube._Picture__obj):
                return True
        for tube in self.__tubes_op:
            if self.__bird._Picture__obj.colliderect(tube._Picture__obj):
                return True
        if self.__bird._Picture__obj.colliderect(self.__sand._Picture__obj):
            return True
        return False

    def run(self):
        while self.__running:
            self.__clock.tick(60)
            self.__screen.fill(Color.WHITE)
            self.__background.draw()
            self.__sand.draw(self.__end_point)

            if self.__end_point <= -400:
                self.__end_point = 0
            self.__end_point -= self.__Vx

            for tube in self.__tubes:
                if tube.x <= -tube.width:
                    tube.reset()
                    tube.x = 550
                if tube.x + tube.width < self.__bird.x and not tube.passed:
                    self.score += 1
                    tube.passed = True
                tube.x -= self.__Vx
                tube.draw()
            for tube_op in self.__tubes_op:
                tube_op.draw()

            self.__bird.y += self.__Vy
            self.__Vy += self.__gravity
            self.__bird.draw()

            self.draw_score()

            if self.check_bird_colliderect_objects():
                self.__bird.draw()
                self.draw_game_over()
                if not self.__pausing:
                    sleep(0.25)
                    pygame.event.clear()
                self.pausing = True
                self.__game_over = True

            if not self.__game_over and self.pausing:
                self.draw_instruction()

            # Xử lý sự kiện người dùng
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.pausing:
                            if self.__game_over:
                                # pygame.mixer.unpause()
                                self.__bird.reset()
                                for tube in self.__tubes:
                                    tube.reset()
                                self.score = 0
                                self.__game_over = False
                            else:
                                self.pausing = False
                                self.__Vy = -7
                        else:
                            self.__Vy = -7
                            
            pygame.display.flip()
        pygame.quit()