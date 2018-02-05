import pygame, sys

class Game(object):

    def __init__(self):
        # Config
        self.tps_max = 60.0

        # Init
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.delta = 0.0

        while True:

            # Handle Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.delta += self.clock.tick()/1000
            while self.delta >= 1/self.tps_max:
                self.delta -= 1/self.tps_max

            # Drawing
            self.screen.fill((0, 0, 0))
            self.render()
            pygame.display.flip()

    def tick(self):
        # Input
        keys = pygame.key.get_pressed()


    def render(self):
        # Drawing
        pygame.draw.rect(self.screen,(50,100,200),pygame.Rect(0,0,25,25))

if __name__ == "__main__":
    Game()