import pygame
from code.game import Game
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Girls vs Zombies')

game: Game = Game(window)

game.run()

