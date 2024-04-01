#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:50:13 2024

@author: joaking

Player pixelart from "Puddin - 8 Bit Personalized Alphabet (Only Letters)"

"""

import pygame

PLAYER_X_POS = 35
PLAYER_Y_POS = 30


class Player(pygame.sprite.Sprite):
    def __init__(self, player_num):
        super().__init__()
        self.playerNumber = player_num
        self.score = 0
        self.isReducedDice = False
        self.isActivePlayer = False
        self.isEliminated = False
        player_active = pygame.image.load(f"art/player/player{self.playerNumber}.png").convert_alpha()
        player_inactive = pygame.image.load(f"art/player/player{self.playerNumber}inactive.png").convert_alpha()
        self.playerFrame = (player_inactive, player_active)
        self.image = self.playerFrame[1]
        self.rect = self.image.get_rect(midleft=(PLAYER_X_POS + (155 * (self.playerNumber - 1)), PLAYER_Y_POS))

    def get_player_number(self):
        return self.playerNumber

    def get_score(self):
        return self.score

    def get_is_reduced_dice(self):
        return self.isReducedDice

    # todo to delete if not used
    # def getIsActivePlayer(self):
    #     return self.isActivePlayer

    def get_is_eliminated(self):
        return self.isEliminated

    def activate(self):
        self.isActivePlayer = True

    def deactivate(self):
        self.isActivePlayer = False

    def eliminated(self):
        self.isEliminated = True

    def add_score(self, score_value):
        self.score += score_value

    def update(self):
        self.image = self.playerFrame[self.isActivePlayer]
        return
