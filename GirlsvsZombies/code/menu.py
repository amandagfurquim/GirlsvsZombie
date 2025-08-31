#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import HEY_GIRL_FONT, ZOMBIE_FONT, ARIAL_FONT, WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_PINK, COLOR_BLACK, \
    COLOR_GREEN, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/MenuBattleground4.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, size, text, text_color, text_center_pos, font):
        text_surf = font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(size=100, text="Girls", text_color=COLOR_PINK, text_center_pos=((WINDOW_WIDTH / 2), 70),
                           font=HEY_GIRL_FONT)
            self.menu_text(size=80, text="vs", text_color=COLOR_BLACK, text_center_pos=((WINDOW_WIDTH / 2), 120),
                           font=ARIAL_FONT)
            self.menu_text(size=30, text="Zombies", text_color=COLOR_GREEN, text_center_pos=((WINDOW_WIDTH / 2), 180),
                           font=ZOMBIE_FONT)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(size=30, text=MENU_OPTION[i], text_color=COLOR_PINK,
                                   text_center_pos=((WINDOW_WIDTH / 2), 350 + 45 * i),
                                   font=ARIAL_FONT)
                else:
                    self.menu_text(size=30, text=MENU_OPTION[i],text_color=COLOR_WHITE , text_center_pos=((WINDOW_WIDTH / 2), 350+ 45 * i),
                    font=ARIAL_FONT)

        # CHECA OS EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # tecla para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

            pygame.display.flip()

    # Eu tentei de todos os jeitos criar uma variavel mas não deu certoooo
            def menu_text(self, text_size: 20, text: str, text_color: tuple, text_center_pos: tuple):
                text_font: Font = pygame.font.SysFont(name="asset/Zombie bites", size=text_size)
                text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
                text_rect: Rect = text_surf.get_rect(center=text_center_pos)
                self.window.blit(source=text_surf, dest=text_rect)

