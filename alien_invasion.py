import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.bg_color = (200,200,200)
        ## pygame.display.set_mode is a surface, this particular surface is where game elements will be displayed
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Starting the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                # when player clicks on close button this event is generated and sys.exit() is called to close the window
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()