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
            self._check_events()
            self._update_screen()
            
            #Watch for keyboard and mouse events
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # when player clicks on close button this event is generated and sys.exit() is called to close the window
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                # Move the ship to the right when the right arrow key is pressed
                    self.ship.rect.x += 10
                elif event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 10
    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        #fill background with this colour
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
        self.clock.tick(60)
# read the documentation for pygame.display.flip() to understand why it is used here. It is used to make the most recently drawn screen visible. In this case, it updates the
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()