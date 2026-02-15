import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        ## pygame.display.set_mode is a surface, this particular surface is where game elements will be displayed
        pygame.display.set_caption("Alien Invasion")
        self.ship= Ship(self)

    def run_game(self):
        """Starting the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                # when player clicks on close button this event is generated and sys.exit() is called to close the window
                if event.type == pygame.QUIT:
                    sys.exit()
            #fill background with this colour
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()