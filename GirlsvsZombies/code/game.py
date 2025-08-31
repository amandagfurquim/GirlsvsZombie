#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT

class Game:
    def __init__(self, window):
        self.window = window
        self.menu = Menu(self.window)

    def run(self):



        while True:
            self.window.fill((0, 0, 0))

            self.menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            pygame.display.flip()